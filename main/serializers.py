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
