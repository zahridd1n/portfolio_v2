# Generated by Django 5.1.1 on 2024-10-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_education_body_en_education_body_ru_education_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teach', models.IntegerField(default=0)),
                ('project', models.IntegerField(default=0)),
                ('client', models.IntegerField(default=0)),
                ('company', models.IntegerField(default=0)),
            ],
        ),
    ]