from django.apps import AppConfig
from django.db.models.signals import pre_save

class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'





