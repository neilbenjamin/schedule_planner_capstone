# Import models/sql tables from models.py and the forms modules from Django.

from django import forms
from .models import Event, ContactMessage

# Create a new form sub class that we can build form objects with while tapping
# into Django's powerful pre-built bass or superclasses


class EventForm(forms.ModelForm):
    """
    Form for creating and updating event info
    This form based on the :class:`~planner.models.Event` model and
    inherits from `~django.forms.ModelForm` to generate and create forms.
    :cvar Meta: Inner class to build and host metadata for the form.
    """
    class Meta:
        """
        Metadata for the event form

        :ivar date: Date of the event
        :ivar performance_time_start: Start timeof the performance
        :ivar performance_time_end: End time of the performance
        :ivar venue: Venue for event
        :ivar performer: Name of the performer
        :ivar sound-engineer: Name of the assigned engineer.
        """
        # class attribute relevent to attribute instances
        model = Event
        # Attributes
        fields = [
            'date',
            'performance_time_start',
            'performance_time_end',
            'venue',
            'performer',
            'sound_engineer',
        ]
        # Widgets Dict for UI to pick dates and times
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'performance_time_start': forms.TimeInput(attrs={'type': 'time'}),
            'performance_time_end': forms.TimeInput(attrs={'type': 'time'}),
        }


class ContactForm(forms.ModelForm):
    """
    Form for creating a contact form based off
    :class:`~planner.models.ContactMessage` and is used to build contact forms
    inherited from :class:`~django.forms.Modelform`

    :cvar Meta: Inner class for adding form metadata
    """
    class Meta:
        """
        Inner class for adding metadata
        :ivar name: user's name
        :ivar email: user's email
        :ivar message: user's message
        """
        # Define db model
        model = ContactMessage
        # define fields
        fields = [
            'name',
            'email',
            'message',
            # Will activate when form is live if needed
            # 'is_read',
            # 'replied_to'
        ]
