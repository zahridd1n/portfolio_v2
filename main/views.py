from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from . import models
from . import serializers


# ---------------------------MyData-------------------------------------
def get_my_data():
    aboutme = models.AboutMe.objects.last()
    aboutme_sr = serializers.AboutMeSerializer(aboutme)
    skills = models.Skills.objects.all()
    skills_sr = serializers.SkillsSerializer(skills, many=True)
    language = models.Language.objects.all()
    language_sr = serializers.LanguageSerializer(language, many=True)
    social_media = models.SocialMedia.objects.all()
    social_media_sr = serializers.SocialMediaSerializer(social_media, many=True)
    technology = models.Technology.objects.all()
    technology_sr = serializers.TechnologySerializer(technology, many=True)

    data = {
        'aboutme': aboutme_sr.data,
        'skills': skills_sr.data,
        'language': language_sr.data,
        'social_media': social_media_sr.data,
        'technology': technology_sr.data,
    }
    return data


@api_view(['GET'])
def my_data(request):
    data = get_my_data()
    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Home page-----------------------------------

@api_view(['GET'])
def home_page(request):
    services = models.Service.objects.all()
    services_sr = serializers.ServiceSerializer(services, many=True)
    recommend = models.Recommend.objects.all()
    recommend_sr = serializers.RecommendSerializer(recommend, many=True)
    my_state = models.MyStat.objects.last()
    my_state_sr = serializers.MyStatSerializer(my_state)

    data = {
        'services': services_sr.data,
        'recommend': recommend_sr.data,
        'my_state': my_state_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })



# -----------------------------Portfolio page-----------------------------------

@api_view(['GET'])
def portfolio_page(request):
    projects = models.Project.objects.all()
    projects_sr = serializers.ProjectSerializer(projects, many=True)

    data = {
        'projects': projects_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })

# -----------------------------Portfolio detail page-----------------------------------

@api_view(['GET'])
def project_page(request, project_id):
    project = get_object_or_404(models.Project, pk=project_id)
    project_sr = serializers.ProjectSerializer(project)

    data = {
        'project': project_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Education page-----------------------------------

@api_view(['GET'])
def education_page(request):
    education = models.Education.objects.all()
    education_sr = serializers.EducationSerializer(education, many=True)

    data = {
        'education': education_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Education page-----------------------------------

@api_view(['GET'])
def experience_page(request):
    experience = models.Experience.objects.all()
    experience_sr = serializers.ExperienceSerializer(experience, many=True)

    data = {
        'experience': experience_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })

