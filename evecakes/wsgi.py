"""
WSGI config for evecakes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from .settings import BASE_DIR


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evecakes.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'media'))
application.add_files(os.path.join(BASE_DIR, 'media'), prefix='uploads/')
