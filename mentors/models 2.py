from django.db import models
from datetime import datetime

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name


