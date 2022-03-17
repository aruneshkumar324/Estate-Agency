from django.db import models
from datetime import datetime


class Inquiry(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)
    interested = models.CharField(max_length=250)
    car_title = models.CharField(max_length=250)
    message = models.TextField()
    user_id = models.CharField(max_length=250)
    car_id = models.CharField(max_length=250)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email