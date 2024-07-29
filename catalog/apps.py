from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'


class PostConfig(AppConfig):
    name = 'post'
    default_auto_field = 'django.db.models.BigAutoField'
