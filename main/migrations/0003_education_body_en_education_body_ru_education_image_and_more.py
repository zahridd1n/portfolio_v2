# Generated by Django 5.1.1 on 2024-10-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_education_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='body_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='body_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='education/'),
        ),
        migrations.AddField(
            model_name='education',
            name='major_en',
            field=models.CharField(blank=True, max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='major_ru',
            field=models.CharField(blank=True, max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='university_en',
            field=models.CharField(blank=True, max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='university_ru',
            field=models.CharField(blank=True, max_length=233, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='body_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='body_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Experience/'),
        ),
        migrations.AddField(
            model_name='experience',
            name='position_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='position_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]