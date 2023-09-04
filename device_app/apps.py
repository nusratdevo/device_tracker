from django.apps import AppConfig


class DeviceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'device_app'
   

    def ready(self):
        import device_app.signals 