import replicate
import os
from dotenv import load_dotenv
import tempfile

load_dotenv()

from deep_translator import GoogleTranslator
import openai

client = openai.OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)


def uzbek_prompt_to_english_video_prompt(uzbek_text):
    try:
        # OpenAI yordamida o'zbekcha promptni ingliz tiliga tarjima qilish + professional video promptga aylantirish
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a multilingual prompt converter. When given a prompt in Uzbek language, accurately translate it into English."
                        " Then write a simple and direct prompt for video generation, describing only the core action or gesture like 'two men shaking hands' or 'a girl waving'."
                        " Do not describe the background in detail. Avoid unnecessary cinematic setting or mood descriptions. Keep it simple and clear for AI video generation."
                    )
                },
                {
                    "role": "user",
                    "content": uzbek_text
                }
            ]
        )

        full_output = response.choices[0].message.content.strip()
        # Faqat professional promptni olish (ikkinchi bo‘lak)
        only_prompt = full_output.split("\n\n")[-1].strip()
        return only_prompt

    except Exception as e:
        return f"Xato yuz berdi: {str(e)}"



def generate_video_from_file(image_file, uzbek_prompt):
    english_prompt = uzbek_prompt_to_english_video_prompt(uzbek_prompt)

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
