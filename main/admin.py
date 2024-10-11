from django.contrib import admin
from .models import AboutMe, Service, Skills, Language
from . import models


# Register your models here.

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'region', 'city', 'age',)
    list_filter = ('region', 'city', 'age',)
    list_display_links = ('id', 'full_name', 'region', 'city',)
    search_fields = ('full_name', 'region', 'city')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_ru', 'title_en', 'description', 'description_ru', 'description_en')
    list_filter = ('title', 'title_ru', 'title_en')
    list_display_links = ('id', 'title', 'title_ru', 'title_en')
    search_fields = ('title', 'title_ru', 'title_en',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage')
    list_filter = ('name', 'percentage')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percentage')
    list_filter = ('name', 'percentage')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(models.Recommend)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.MyStat)
admin.site.register(models.SocialMedia)
admin.site.register(models.Technology)
admin.site.register(models.Portfolio_Category)
admin.site.register(models.Project)
admin.site.register(models.Banner)
admin.site.register(models.RecommendedSocial)


