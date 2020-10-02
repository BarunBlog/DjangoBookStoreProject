"""
WSGI config for bookstore_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('<bookstore_project>/')
sys.path.append('<bookstore_project>/users')
#sys.path.append('<bookstore_project>/pages')
#sys.path.append('<bookstore_project>/orders')

os.environ['DJANGO_SETTINGS_MODULE'] = 'bookstore_project.bookstore_project.settings'

application = get_wsgi_application()
