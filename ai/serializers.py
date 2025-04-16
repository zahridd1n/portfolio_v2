from rest_framework import serializers
from . import models

class PriceSR(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = '__all__'

class GeneratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Generated
        fields = '__all__'
        read_only_fields = ['video', 'created_at']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = ['id', 'user', 'price', 'date']
        read_only_fields = ['user', 'date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'first_name', 'credit']

