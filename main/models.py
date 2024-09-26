from django.db import models


class AboutMe(models.Model):
    ...


class Service(models.Model):
    title = models.CharField(max_length=50)
    title_ru = models.CharField(max_length=50, blank=True, null=True)
    title_en = models.CharField(max_length=50, blank=True, null=True)

    description = models.TextField()
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=25)
    percentage = models.FloatField(default=0)

    def __str__(self):
        return self.name
