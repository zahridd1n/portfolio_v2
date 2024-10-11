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
        fields = ['id', 'name', 'image', 'title', 'description', 'mark','get_socials']

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
        fields = ['image', 'full_name', 'profession', 'region', 'city', 'age']


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


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'
