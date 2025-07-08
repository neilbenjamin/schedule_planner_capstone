from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class SignUpForm(UserCreationForm):
    """
    Form for user registration, extending Django's built-in UserCreationForm.

    This form allows users to create new accounts with additional fields
    beyond the default username and password, specifically first name,
    last name, and email. It is designed to work with Django's
    custom user model.

    :param first_name: User's first name (CharField).
    :type first_name: str
    :param last_name: User's last name (CharField).
    :type last_name: str
    :param email: User's email address (EmailField).
    :type email: str
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta(UserCreationForm.Meta):
        """
        Meta options for the SignUpForm.

        This inner class defines the associated model and the fields
        to be displayed and managed by the form.

        :param model: The Django model that this form is associated with.
                      It is set to Django's currently active user model.
        :type model: class
        :param fields: A tuple of field names to be included in the form.
                       It extends the default UserCreationForm fields
                       with 'first_name', 'last_name', and 'email'.
        :type fields: tuple
        """
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('first_name',
                                                 'last_name',
                                                 'email')
