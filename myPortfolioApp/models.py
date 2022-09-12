from django.utils import timezone
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100, unique=True)
    link = models.CharField(max_length=160, blank=True)
    description = models.TextField()  # Blank=True means optional
    cover_image = models.ImageField(upload_to='images/portfolio/', blank=True)
    gallery_image_one = models.ImageField(upload_to='images/portfolio/', blank=True)
    gallery_image_two = models.ImageField(upload_to='images/portfolio/', blank=True)
    is_available = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title 

