from django.conf.urls import patterns, include, url
from Index.views import main

# Uncomment the next two lines to enable the admin:


urlpatterns = patterns('',
	url(r'^$','Index.views.main'),   
)
