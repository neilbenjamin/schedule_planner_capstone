from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration for the accounts django application and defines the
    metadata and settings for the 'accounts' app, allowing django to access
    and manage it.

    :param default_auto_field: Specifies the default PK field type for the
                               models in this app to BigAutoField
    :param name: The python path to this app, used by Django for referencing

    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
