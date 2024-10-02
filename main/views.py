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

    data = {
        'services': services_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data

    })
