"""

Django settings for webcookies project.

"""

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



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_u&x@pjymdrpfkil(kg!mix#h-&18h#dn@j!7y%skb%qnxn1q@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'socialcookies'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangomako.middleware.MakoMiddleware'
)

#########
#NOTA: Cambiar la ruta para alojar la aplicacion en otro servidor
#
#TEMPLATE_DIRS = ( '<ruta_proyecto>/SocialCookies/ENV1/webcookies/socialcookies/templates/socialcookies' )
#########
TEMPLATE_DIRS = (
                    BASE_DIR + '/socialcookies/templates/socialcookies'
)

ROOT_URLCONF = 'webcookies.urls'

WSGI_APPLICATION = 'webcookies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'socialcookiesiv@gmail.com'
EMAIL_HOST_PASSWORD = 'IVsocialcookies'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
