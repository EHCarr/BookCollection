from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 150)
    author = models.CharField(max_length= 150)
    description = models.CharField(max_length = 1000)
    read = models.BooleanField(default='None')
    image = models.ImageField(upload_to='main_app/static/uploads/', default='no image')

