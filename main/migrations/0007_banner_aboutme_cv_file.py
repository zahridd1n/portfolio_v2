# Generated by Django 5.1.1 on 2024-10-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_technolgy_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_ru', models.CharField(blank=True, max_length=50, null=True)),
                ('title_en', models.CharField(blank=True, max_length=50, null=True)),
                ('text1', models.CharField(max_length=30)),
                ('text1_ru', models.CharField(blank=True, max_length=30, null=True)),
                ('text1_en', models.CharField(blank=True, max_length=30, null=True)),
                ('text2', models.CharField(max_length=30)),
                ('text2_ru', models.CharField(blank=True, max_length=30, null=True)),
                ('text2_en', models.CharField(blank=True, max_length=30, null=True)),
                ('text3', models.CharField(max_length=30)),
                ('text3_ru', models.CharField(blank=True, max_length=30, null=True)),
                ('text3_en', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='aboutme',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='about/cv_files/', verbose_name='cv_files'),
        ),
    ]
