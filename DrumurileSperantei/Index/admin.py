from django.contrib import admin
from Index.models import Article
from django.contrib.sites.models import Site
from Index.models import TitlulZilei
from Index.models import Picture
from Index.models import TitlulZileiTab
from Index.models import *
from django.contrib.auth.models import Group
from django.contrib.flatpages.models import FlatPage 



#from django.contrib.sites.models import Groups
#class Slug(admin.ModelAdmin):
#	prepopulated_fields = {'slug':('title',)}


	

class Article_A(admin.ModelAdmin):
	#pass	
	fieldsets = (
		(None,{
			'fields':('categorie',)
			}),
		(None,{
			'fields':('title','author','date_published','text')
			}),
		(None,{
			
			'fields':('art_picture','slug','is_active')
			}),
		)
	list_display = ['title','author','date_published','image_thumb','categorie','slug','text','is_active']
	list_filter = ['date_published','author']
	search_fields = ['author','title']
	actions_selection_counter = True
		

    
class TitlulZilei_A(admin.ModelAdmin):
	list_display = ['site_title',]
	list_filter = ['date_published',]

class TitlulZileiTab_A(admin.ModelAdmin):
	list_display = ['site_titletab',]
	list_filter = ['date_published',]

class Image(admin.ModelAdmin):
	Upload = 'picture'

class Category_A(admin.ModelAdmin):
	exclude = ('slug',)
	list_display =  ['title','slug']
    
	

admin.site.register(Article,Article_A)
admin.site.unregister(Site)
admin.site.register(TitlulZilei,TitlulZilei_A)
admin.site.register(Picture,Image)
admin.site.register(TitlulZileiTab,TitlulZileiTab_A)
admin.site.register(Category, Category_A)
admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.unregister(Group)
#admin.site.register(Article,Slug)
#admin.site.unregister(Groups)
#admin.site.unregister(Taggit)
