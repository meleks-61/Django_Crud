from django.apps import AppConfig


class Blog3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog3'
    
    def ready(self):
        import blog3.signals
