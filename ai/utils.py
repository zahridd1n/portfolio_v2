import replicate
import os
from dotenv import load_dotenv
import tempfile

load_dotenv()

from deep_translator import GoogleTranslator
import openai

client = openai.OpenAI(
    api_key="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",
    # <-- o'zingizning API kalitingizni kiriting
    base_url="https://openrouter.ai/api/v1"
)


def uzbek_to_english_video_prompt(uzbek_text):
    try:
        # Tarjima qilish (o'zbekchadan inglizchaga)
        translator = GoogleTranslator(source='uz', target='en')
        english_text = translator.translate(uzbek_text)

        # Promptni video generatsiyasi uchun tasviriy va professional shaklga keltirish
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # Eng yangi model, agar mavjud bo'lmasa "gpt-4" ishlatiladi
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert prompt engineer specializing in creating concise, vivid, and detailed prompts for video generation AI tools like Runway or Kaiber. "
                        "Take the user's input and transform it into a short, descriptive English video prompt (50-70 words) with rich visual details, cinematic style, and clear elements, suitable for generating high-quality videos."
                    )
                },
                {
                    "role": "user",
                    "content": f"Enhance this description into a concise video prompt: {english_text}"
                }
            ]
        )

        improved_prompt = response.choices[0].message.content
        print('prompt', improved_prompt)
        return improved_prompt

    except Exception as e:
        return f"Xato yuz berdi: {str(e)}"


def generate_video_from_file(image_file, uzbek_prompt):
    english_prompt = uzbek_to_english_video_prompt(uzbek_prompt)

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        for chunk in image_file.chunks():
            tmp.write(chunk)
        tmp_path = tmp.name

    # Modelga yuborish uchun faylni o'qish
    with open(tmp_path, "rb") as img:
        input_data = {
            "image": img,
            "prompt": english_prompt,
        }

        # Replicate API orqali video yaratish
        output = replicate.run(
            "wavespeedai/wan-2.1-i2v-480p",
            input=input_data
        )

    os.unlink(tmp_path)

    return output
