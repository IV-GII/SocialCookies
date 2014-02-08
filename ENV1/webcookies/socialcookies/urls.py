# Copyright (C) 2014  SocialCookies @IV/GII

# @anaprados @oskyar @torresj @josemlp91
# @franciscomanuel @rogegg  @pedroag  @melero90

# Aplicacion web, para gestionar pedidos de galletas,
# con fotos de Instagram y Twitter. 

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.



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
