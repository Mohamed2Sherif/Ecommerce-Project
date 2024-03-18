import os

from celery import Celery

from src.products.Services.PServices import ProductService
# Set the default Django settings module for the 'celery' program.
BUILD_ENVIRONMENT = os.environ.get('BUILD_ENVIRONMENT', 'local').lower()
if  BUILD_ENVIRONMENT=="local" : 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
else : 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

app = Celery()

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.register_task(ProductService)


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')