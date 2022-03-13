from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=200)
    author = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='blog/%Y/%m/%d/')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title