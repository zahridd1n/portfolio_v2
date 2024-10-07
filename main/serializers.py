from rest_framework import serializers
from . import models


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommend
        fields = '__all__'


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