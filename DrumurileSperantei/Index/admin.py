from django.contrib import admin
from Index.models import Article
from django.contrib.sites.models import Site
from Index.models import RenameTitle
from Index.models import Picture

#from django.contrib.sites.models import Groups

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','author','date_published','art_picture','tags']
	list_filter = ['date_published','author']
	search_fields = ['author','title']
	#date_published_hierarchy = 'created'
	save_on_top = True
    
class P2Admin(admin.ModelAdmin):
	list_display = ['site_title',]
	class Meta:
		verbose_name = 'Rename Title'

class Image(admin.ModelAdmin):
	Upload = 'picture'
	

admin.site.register(Article,PostAdmin)
admin.site.unregister(Site)
admin.site.register(RenameTitle,P2Admin)
admin.site.register(Picture,Image)
#admin.site.unregister(Groups)
#admin.site.unregister(Taggit)
