from django.db import models
from ckeditor.fields import RichTextField


class Agent(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    intro = RichTextField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    facebook_link = models.URLField(max_length=300)
    twitter_link = models.URLField(max_length=300)
    instagram_link = models.URLField(max_length=300)
    linkedin_link = models.URLField(max_length=300)
