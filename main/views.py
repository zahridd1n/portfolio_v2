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
def home_page(request, lang=None):
    banner = models.Banner.objects.last()
    banner_sr = serializers.BannerSerializer(banner, context={'lang': lang})
    services = models.Service.objects.all()
    services_sr = serializers.ServiceSerializer(services, many=True, context={'lang': lang})
    recommend = models.Recommend.objects.all()
    recommend_sr = serializers.RecommendSerializer(recommend, many=True, context={'lang': lang})
    my_state = models.MyStat.objects.last()
    my_state_sr = serializers.MyStatSerializer(my_state)

    data = {
        'banner_data': banner_sr.data,
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
def portfolio_page(request, lang=None):
    category = models.Portfolio_Category.objects.all()
    category_sr = serializers.CategorySerializer(category, many=True)
    projects = models.Project.objects.all()
    projects_sr = serializers.ProjectSerializer(projects, many=True, context={'lang': lang})

    data = {
        'portfolio_category': category_sr.data,
        'projects': projects_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Portfolio detail page-----------------------------------

@api_view(['GET'])
def project_page(request, project_id, lang=None):
    project = get_object_or_404(models.Project, pk=project_id)
    project_sr = serializers.ProjectSerializer(project, context={'lang': lang})
    my_state = models.MyStat.objects.last()
    my_state_sr = serializers.MyStatSerializer(my_state)
    data = {
        'project': project_sr.data,
        'my_state': my_state_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Education page-----------------------------------

@api_view(['GET'])
def education_experience(request, lang=None):
    education = models.Education.objects.all().order_by('-start_date')
    education_sr = serializers.EducationSerializer(education, many=True, context={'lang': lang})
    experience = models.Experience.objects.all().order_by('-start_date')
    experience_sr = serializers.ExperienceSerializer(experience, many=True, context={'lang': lang})
    data = {
        'education': education_sr.data,
        'experience': experience_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })


# -----------------------------Contact--------------------------------
@api_view(['GET'])
def contact_page(request, lang=None):
    contact_data = models.AboutMe.objects.last()
    contact_data_sr = serializers.ContactDataSerializer(contact_data, context={'lang': lang})

    data = {
        'contact_data': contact_data_sr.data,
    }

    return Response({
        'success': True,
        'message': 'success',
        'data': data
    })
