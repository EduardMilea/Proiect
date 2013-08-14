from django.conf.urls import patterns, include, url
from Index.views import MainView
from Index.views import CategoryView
from Index.views import PostView
# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
	
	url(r'^$',MainView.as_view()),
	url(r'^categories/(?P<category_slug>[A-Za-z0-9-_.]+)/$', CategoryView.as_view(), name="category_view"),
	url(r'^post/(?P<slug>[A-Za-z0-9-_.]+)/$',PostView.as_view()),

	

	#url(r'^favicon\.ico$', 
    #'django.views.generic.simple.redirect_to', 
    #{'url': '/home/eduard/Proiect/DrumurileSperantei/Index/favicon.ico'}),  
)
