from distutils.command.upload import upload
from django.utils import timezone
from django.db import models

# Create your models here.
class GithubItem(models.Model):
    repository_name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100, unique=True)
    repository_link = models.CharField(max_length=160)
    description = models.TextField()  # Blank=True means optional
    repository_thumbnail = models.ImageField(upload_to='images/repositories/', blank=True)
    repository_image_one = models.ImageField(upload_to='images/repositories/', blank=True)
    repository_image_two = models.ImageField(upload_to='images/repositories/', blank=True)
    is_available = models.BooleanField(default=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.repository_name 