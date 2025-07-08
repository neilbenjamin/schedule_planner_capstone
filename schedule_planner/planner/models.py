from django.db import models

# Create your models here.

# New sound engineer model linked to Event one to many as a foreign
# key.


class SoundEngineer(models.Model):
    """
    Represents a sound engineer who can be assigned to various events.

    :ivar name: The unique name of the sound engineer.
    :vartype name: str
    :ivar contact_email: The contact email address of the sound engineer.
    :vartype contact_email: str (EmailField)
    :ivar contact_number: The unique contact number of the sound engineer.
    :vartype contact_number: str
    """
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the sound engineer.

        :returns: The name of the sound engineer.
        :rtype: str
        """
        return self.name

    class Meta:
        """
        Meta options for the SoundEngineer model.
        """
        ordering = ['name']


class Event(models.Model):
    """
    Represents a single event with its booking details and assigned
    sound engineer.

    :ivar date: The date of the event.
    :vartype date: date
    :ivar performance_time_start: The start time of the performance.
    :vartype performance_time_start: time
    :ivar performance_time_end: The end time of the performance.
    :vartype performance_time_end: time
    :ivar venue: The name of the venue where the event takes place.
    :vartype venue: str
    :ivar performer: The name of the performer for the event.
    :vartype performer: str
    :ivar sound_engineer: A foreign key to the :class:`~.SoundEngineer` model,
                         representing the assigned sound engineer. Can be null.
    :vartype sound_engineer: :class:`~.SoundEngineer`
    :ivar event_notes: Additional notes or details for the event. (Optional)
    :vartype event_notes: str (TextField)
    """
    # Table Col data
    date = models.DateField()
    performance_time_start = models.TimeField(verbose_name="Start Time")
    performance_time_end = models.TimeField(verbose_name="End Time")
    venue = models.CharField(max_length=100)
    performer = models.CharField(max_length=100)
    sound_engineer = models.ForeignKey(SoundEngineer,
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True,
                                       related_name='events_as_engineer')
    event_notes = models.TextField(verbose_name="Event notes",
                                   blank=True, null=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the sound engineer.

        :returns: The name of the sound engineer.

        :rtype: str
        """
        return f"{self.performer} on {self.date} in {self.venue}"

    class Meta:
        ordering = ['date', 'performance_time_start']
        permissions = [
            ("can_manage_event_engineer", "can_assign_engineers")
        ]


class ContactMessage(models.Model):
    """
    Represents a contact message submitted by a user through a form.

    This model stores message content, sender details, creation timestamp,
    and flags for tracking its read and replied-to status.

    :ivar name: The name of the person who sent the message.
    :vartype name: str
    :ivar email: The email address of the sender.
    :vartype email: str (EmailField)
    :ivar message: The content of the message.
    :vartype message: str (TextField)
    :ivar created_at: The date and time when the message was created.
                      Automatically set on creation.
    :vartype created_at: datetime.datetime
    :ivar is_read: A boolean flag indicating if the message has been read.
    :vartype is_read: bool
    :ivar replied_to: A boolean flag indicating if a reply has been sent.
    :vartype replied_to: bool
    """
    # Content of table
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Your email address")
    message = models.TextField(verbose_name="Your message")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    replied_to = models.BooleanField(default=False)
    # format for admin

    def __str__(self):
        """
        Returns a human-readable string representation of the contact message.

        :returns: A string indicating the sender's name and the formatted
         creation time.
        :rtype: str
        """
        formatted_time = self.created_at.strftime('%B %d, %Y at %I:%M %p')
        return f"from {self.name} on {formatted_time}"
