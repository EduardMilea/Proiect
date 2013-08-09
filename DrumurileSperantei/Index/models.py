from urlparse  import urlparse
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from taggit.managers import TaggableManager

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date_published = models.DateTimeField()
    text = models.TextField()
    art_picture = models.ImageField(upload_to = 'art_pict')
    tags = TaggableManager()
    #image = models.ImageField(upload_to='Images',height_field = 250, width_field = 250)

class RenameTitle(models.Model):
	site_title = models.CharField(max_length = 50)


class Picture(models.Model):
	picture = models.ImageField(upload_to = 'pictures')




    
    
    
    
    