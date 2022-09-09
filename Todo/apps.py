from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Todo'
    
    #installed signals
    def ready(self):
      import Todo.signals