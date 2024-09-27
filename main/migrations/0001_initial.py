# Generated by Django 5.1.1 on 2024-09-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='fullname')),
                ('region', models.CharField(max_length=255, verbose_name='region')),
                ('city', models.CharField(max_length=255, verbose_name='city')),
                ('age', models.IntegerField(verbose_name='age')),
                ('choice', models.IntegerField(choices=[('frontend', 'frontend'), ('backend', 'backend')], verbose_name='choice')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('title_en', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('percentage', models.FloatField(default=0)),
            ],
        ),
    ]
