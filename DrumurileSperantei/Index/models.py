from urlparse  import urlparse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date_published = models.DateTimeField()
    text = models.TextField()
    #image = models.ImageField(upload_to='Images',height_field = 250, width_field = 250)

    
    
    
    
    