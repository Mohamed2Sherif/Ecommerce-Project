"""
ASGI config for OLA_Store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "src"))

BUILD_ENVIRONMENT = os.environ.get('BUILD_ENVIRONMENT', 'local').lower()
if  BUILD_ENVIRONMENT=="local" : 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
else : 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

application = get_asgi_application()
