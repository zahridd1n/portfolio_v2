from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    credit = models.FloatField(default=0)


class Price(models.Model):
    name = models.CharField(max_length=122)
    price = models.IntegerField(default=0)
    credit = models.IntegerField(null=True, blank=True)
    body = models.TextField()
    is_popular = models.BooleanField(default=False)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Generated(models.Model):
    image = models.ImageField(upload_to='images/')
    prompt = models.TextField()
    is_trand = models.BooleanField(default=False)
    video_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending', null=True, blank=True)
    def __str__(self):
        return f"{self.prompt[:30]}"