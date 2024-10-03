from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from . import models
from . import serializers


# ----------------------Asosiy sahifa----------------------
@api_view(['GET'])
def home_page(request):
    services = models.Service.objects.filter()
    services_sr = serializers.ServiceSerializer(services, many=True)
    recommend = models.Recommend.objects.filter()
    recommend_sr = serializers.RecommendSerializer(recommend, many=True)
    my_state = models.MyStat.objects.last()
    my_state_sr = serializers.MyStatSerializer(my_state)

    data = {
        'services': services_sr.data,
        'recommend': recommend_sr.data,
        'my_state': my_state_sr.data
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data

    })
