from django.apps import AppConfig


class CareersConfig(AppConfig):
    name = 'careers'

    def ready(self):
        import careers.signals

