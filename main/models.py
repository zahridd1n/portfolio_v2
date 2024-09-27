from django.db import models


class AboutMe(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='fullname')
    region = models.CharField(max_length=255, verbose_name='region')
    city = models.CharField(max_length=255, verbose_name='city')
    age = models.IntegerField(verbose_name='age')
    profession = models.TextField(verbose_name='profession')
    phone = models.CharField(max_length=255, verbose_name='phone')
    email = models.EmailField(verbose_name='email')
    address = models.TextField(verbose_name='address')

    def __str__(self):
        return self.full_name


class  SocialMedia(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField()
    image = models.ImageField(verbose_name='image')

    def __str__(self):
        return self.name

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

class Language(models.Model):
    name = models.CharField(max_length=25)
    percentage = models.IntegerField()

    def __str__(self):
         return self.name

class Portfolio_Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Portfolio_Category, on_delete=models.CASCADE)
    image1 = models.ImageField(verbose_name='image')
    image2 = models.ImageField(verbose_name='image', upload_to='image/', blank=True, null=True)
    image3 = models.ImageField(verbose_name='image', upload_to='image/', blank=True, null=True)
    image4 = models.ImageField(verbose_name='image', upload_to='image/', blank=True, null=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    # status = models.
    def __str__(self):
        return self.title