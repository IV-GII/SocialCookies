from django.conf.urls import patterns, url

from socialcookies import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'instagram', views.instagram, name='instagram'),
    url(r'twitter', views.twitter, name='twitter'),
    url(r'contacto', views.contacto, name='contacto'),
    
)
