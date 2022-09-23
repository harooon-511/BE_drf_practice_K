from django.apps import AppConfig
from fcm_django.settings import FCM_DJANGO_SETTINGS as SETTINGS


class AppKConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_k"
    verbose_name = SETTINGS["APP_VERBOSE_NAME"]
    