"""
WSGI config for api_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys

root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'api_project'))
sys.path.insert(0, root_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project/settings')

application = get_wsgi_application()

