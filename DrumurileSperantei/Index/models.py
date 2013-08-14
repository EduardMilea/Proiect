from urlparse  import urlparse
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import permalink


class ActiveManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(is_active=True)

#-------------------------------------------------------------------------------------------

class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date_published = models.DateTimeField()
    text = models.TextField()
    art_picture = models.ImageField(upload_to = 'art_pict')
    #tags = TaggableManager()
    slug = models.SlugField(null = True, blank = True)
    is_active = models.BooleanField()
    categorie = models.ForeignKey('Index.Category')
    objects = ActiveManager()
   
    class Meta:
        verbose_name_plural = 'Articole'
    def __unicode__(self):
        return u'%s' %self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save()
    
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.art_picture)
    image_thumb.allow_tags = True

#------------------------------------------------------------------------------------------
class Category (models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(null = True, blank = True)
    def __unicode__(self):
        return u'%s' %self.title
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save()
    
    def get_absolute_url(self):
        return reverse('category_view',  args=[self.slug])

    class Meta:
        verbose_name_plural = 'Categorii'
    

#-------------------------------------------------------------------------------------------

class TitlulZilei(models.Model):
    date_published = models.DateTimeField()
    site_title = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = 'Titlul Zilei'

#-------------------------------------------------------------------------------------------
    

class TitlulZileiTab(models.Model):
    date_published = models.DateTimeField()
    site_titletab = models.CharField(max_length = 50)
    class Meta:
        verbose_name_plural = 'Titlul Browserului'

#-------------------------------------------------------------------------------------------



class Picture(models.Model):
	picture = models.ImageField(upload_to = 'pictures')




    
    
    
    
    