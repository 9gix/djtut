from django.apps import AppConfig


class CatalogAppConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        import catalog.signals
