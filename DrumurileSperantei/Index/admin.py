from django.contrib import admin
from Index.models import Article

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','author']
	list_filter = ['date_published','author']
	search_fields = ['author','title']
	#date_hierarchy = 'created'
	save_on_top = True

admin.site.register(Article,PostAdmin)

