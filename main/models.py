from django.db import models


class AboutMe(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='fullname')
    region = models.CharField(max_length=255, verbose_name='region')
    city = models.CharField(max_length=255, verbose_name='city')
    address = models.CharField(max_length=255,verbose_name='address', null=True, blank=True)
    age = models.IntegerField(verbose_name='age')
    profession = models.CharField(max_length=122, verbose_name='profession')
    phone = models.CharField(max_length=255, verbose_name='phone')
    email = models.EmailField(verbose_name='email')
    image = models.ImageField(verbose_name='image', upload_to='about/image/', null=True, blank=True)
    cv_file = models.FileField(verbose_name='cv_files', upload_to='about/cv_files/', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Banner(models.Model):
    title = models.CharField(max_length=50)
    title_ru = models.CharField(max_length=50, blank=True, null=True)
    title_en = models.CharField(max_length=50, blank=True, null=True)

    text1 = models.CharField(max_length=30)
    text1_ru = models.CharField(max_length=30, blank=True, null=True)
    text1_en = models.CharField(max_length=30, blank=True, null=True)
    text2 = models.CharField(max_length=30)
    text2_ru = models.CharField(max_length=30, blank=True, null=True)
    text2_en = models.CharField(max_length=30, blank=True, null=True)
    text3 = models.CharField(max_length=30)
    text3_ru = models.CharField(max_length=30, blank=True, null=True)
    text3_en = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
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


class Technology(models.Model):
    name = models.CharField(max_length=25)

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


class Recommend(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recommend/')

    title = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField()
    description_ru = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)

    mark = models.IntegerField(null=True, blank=True, default=0, )

    def save(self, *args, **kwargs):
        if self.mark < 0 or self.mark > 5:  # Ensure mark is between 0 and 5
            self.mark = 0  # or set it to a default value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def get_socials(self):
        return RecommendedSocial.objects.filter(recommend=self)


class RecommendedSocial(models.Model):
    recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    link = models.URLField()
    image = models.ImageField(upload_to='recommended_social/', null=True, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=233)
    position_ru = models.CharField(max_length=100, blank=True, null=True)
    position_en = models.CharField(max_length=100, blank=True, null=True)

    company = models.CharField(max_length=233)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='Experience/', null=True, blank=True)

    body = models.TextField()
    body_ru = models.TextField(blank=True, null=True)
    body_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.position


class Education(models.Model):
    major = models.CharField(max_length=233)
    major_ru = models.CharField(max_length=233, blank=True, null=True)
    major_en = models.CharField(max_length=233, blank=True, null=True)

    university = models.CharField(max_length=233)
    university_ru = models.CharField(max_length=233, blank=True, null=True)
    university_en = models.CharField(max_length=233, blank=True, null=True)

    body = models.TextField()
    body_ru = models.TextField(blank=True, null=True)
    body_en = models.TextField(blank=True, null=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='education/', blank=True, null=True)
    diplom = models.ImageField(upload_to='diplome/', blank=True, null=True)

    def __str__(self):
        return self.university


class MyStat(models.Model):
    teach = models.IntegerField(default=0)
    project = models.IntegerField(default=0)
    client = models.IntegerField(default=0)
    company = models.IntegerField(default=0)

