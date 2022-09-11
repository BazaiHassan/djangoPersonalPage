from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.
class GithubItem(models.Model):
    repository_name = models.CharField(max_length=80)
    slug = models.CharField(max_length=100, unique=True)
    repository_link = models.CharField(max_length=160)
    description = models.TextField(blank=True)  # Blank=True means optional
    repository_logo = models.ImageField(upload_to='images/repositories/', blank=True)
    repository_image_one = models.ImageField(upload_to='images/repositories/', blank=True)
    repository_image_two = models.ImageField(upload_to='images/repositories/', blank=True)
    

    def __str__(self):
        return self.repository_name 