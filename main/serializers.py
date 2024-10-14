from rest_framework import serializers
from . import models


class ServiceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = models.Service
        fields = ['id', 'title', 'description', ]

    def get_title(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.title_en
        elif lang == 'ru':
            return obj.title_ru
        else:
            return obj.title

    def get_description(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.description_en
        elif lang == 'ru':
            return obj.description_ru
        else:
            return obj.description


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ['id', 'title', 'text1', 'text2', 'text3']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')
        data = super().to_representation(instance)

        data['title'] = getattr(instance, f"title_{lang}", instance.title)
        data['text1'] = getattr(instance, f"text1_{lang}", instance.text1)
        data['text2'] = getattr(instance, f"text2_{lang}", instance.text2)
        data['text3'] = getattr(instance, f"text3_{lang}", instance.text3)
        return data


class RecommendedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecommendedSocial
        fields = '__all__'


class RecommendSerializer(serializers.ModelSerializer):
    get_socials = RecommendedSocialSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recommend
        fields = ['id', 'name', 'image', 'title', 'description', 'mark', 'get_socials']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')
        data = super().to_representation(instance)

        data['title'] = getattr(instance, f"title_{lang}", instance.title)
        data['description'] = getattr(instance, f"description_{lang}", instance.description)
        return data


class MyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyStat
        fields = ['teach', 'project', 'client', 'company']


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutMe
        fields = ['image', 'full_name', 'profession', 'region', 'city', 'age', 'cv_file']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Technology
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio_Category
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'category', 'image1', 'image2', 'image3', 'image4', 'date_start', 'date_end']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')
        data = super().to_representation(instance)

        data['title'] = getattr(instance, f"title_{lang}", instance.title)
        data['description'] = getattr(instance, f"description_{lang}", instance.description)
        return data


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = ['id', 'major', 'university', 'body', 'start_date', 'end_date', 'image', 'diplom']

    def to_representation(self, instance):
        lang = self.context.get('lang', 'uz')
        data = super().to_representation(instance)

        data['major'] = getattr(instance, f"major_{lang}", instance.major)
        data['university'] = getattr(instance, f"university_{lang}", instance.university)
        data['body'] = getattr(instance, f"body_{lang}", instance.body)
        return data


class ExperienceSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()

    class Meta:
        model = models.Experience
        fields = ['id', 'company', 'image', 'position', 'body', 'start_date', 'end_date']

    def get_position(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.position_en
        elif lang == 'ru':
            return obj.position_ru
        else:
            return obj.position

    def get_body(self, obj):
        lang = self.context.get('lang', 'uz')
        if lang == 'en':
            return obj.body_en
        elif lang == 'ru':
            return obj.body_ru
        else:
            return obj.body


class ContactDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutMe
        fields = ['region', 'city', 'address', 'email', 'phone']
