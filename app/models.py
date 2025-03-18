from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images' , null=True, blank=True )