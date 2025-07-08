from django.apps import AppConfig


class PlannerConfig(AppConfig):
    """
    Configuration for the Planner Django application.

    This class defines metadata and settings for the 'planner' app,
    allowing Django to properly discover and manage it.

    :param default_auto_field: Specifies the default primary key field type
                               for models in this app to BigAutoField.

    :type default_auto_field: str

    :param name: The Python path to this application, used by Django
                 for discovery and referencing.

    :type name: str
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "planner"
