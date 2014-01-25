from django.conf.urls import patterns, url

from socialcookies import views
from socialcookies import photos

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'instagram', photos.instagram, name='instagram'),
    url(r'oauth_callback', photos.on_callback, name='on_callback'),
    url(r'twitter', views.twitter, name='twitter'),
    url(r'contacto', views.contacto, name='contacto'),    
)
