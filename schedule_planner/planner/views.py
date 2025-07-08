from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required, permission_required
from .models import Event, ContactMessage
from .forms import EventForm, ContactForm
# from django.contrib import messages

# Create your views here.


@login_required
def index(request: HttpRequest) -> HttpRequest:
    """
    Displays the main event schedule for logged-in users.

    Events are ordered by date and start time. Superusers see a different
    template ('planner.html') than regular users ('planner_client.html').

    :param request: The HTTP request object.

    :type request: HttpRequest

    :returns: An HTTP response rendering the appropriate schedule HTML page.

    :rtype: HttpRequest
    """
    # Display full entertainment schedule
    events = Event.objects.all().order_by('date', 'performance_time_start')
    context = {
        'events': events,
    }
    if request.user.is_superuser:
        return render(request, 'pages/planner.html', context)
    else:
        return render(request, 'pages/planner_client.html', context)


@login_required
@permission_required('planner.add_event', raise_exception=True)
def add_event(request: HttpRequest) -> HttpRequest:
    """
    Handles adding new events to the database.

    On a GET request, it displays a blank form. On a POST request, it
    validates and saves the submitted event details to the database.
    Requires 'planner.add_event' permission.

    :param request: The HTTP request object (GET or POST).

    :type request: HttpRequest

    :returns: Redirects to the index page on successful save,
              otherwise renders the 'add_event.html' template with the form.

    :rtype: HttpRequest
    """
    # Add new events to Events DB
    # Check CRUD method
    if request.method == 'POST':
        # create instance of EventForm with the values passed in the Http POST
        # object to variable 'form', which will be instatiated/populated with
        # the POSRT data
        form = EventForm(request.POST)
        # Check form validity
        if form.is_valid():
            # Save to DB
            form.save()
            # Redirect thereafter
            return redirect('planner:index')
    # conditional else return a blank form
    else:
        form = EventForm()
    # Serve the initial blank form on the initial GET request.
    return render(request, 'pages/add_event.html', {'form': form})


@login_required
@permission_required('planner.edit_event', raise_exception=True)
def edit_event(request: HttpRequest, pk: int) -> HttpRequest:
    """
    Handles editing existing event records.

    Retrieves an event instance based on its primary key (pk).
    On a POST request, it updates the event details. On a GET request, it
    displays the form pre-filled with the existing event's data.
    Requires 'planner.edit_event' permission.

    :param request: The HTTP request object (GET or POST).

    :type request: HttpRequest

    :param pk: The primary key of the Event instance to be edited.

    :type pk: int

    :returns: Redirects to the index page on successful update,
              otherwise renders the 'add_event.html' template with the form.

    :rtype: HttpRequest
    """
    # Retrieve existing event record or 404 if not found.
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        # Bind/Instantiate object submitted data to form for validation
        # to the class EventForm
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('planner:index')
    else:
        form = EventForm(instance=event)
    return render(request, 'pages/add_event.html', {'form': form})


@login_required
@permission_required('planner.delete_view', raise_exception=True)
def delete_view(request: HttpRequest, pk: int) -> HttpRequest:
    """
    Handles deleting an event record from the database.

    Fetches the event instance by its primary key (pk). On a POST request,
    it deletes the record. On a GET request, it displays a confirmation page.
    Requires 'planner.delete_view' permission.

    :param request: The HTTP request object (GET or POST).

    :type request: HttpRequest

    :param pk: The primary key of the Event instance to be deleted.

    :type pk: int

    :returns: Redirects to the index page after successful deletion,
              otherwise renders the 'confirm_delete.html' template.

    :rtype: HttpRequest
    """
    # Retrieve existing event record from model file with
    #  pk or 404 if not found.
    event = get_object_or_404(Event, pk=pk)
    # Conditional, if POST, delete
    if request.method == 'POST':
        # Update table with delete.
        event.delete()
        # Redirect to desired path.
        return redirect('planner:index')
        # No need for catching the inner Else as the dedault form actin
        # will manage these exceptions if the forms are not valid.
    else:
        # if method is GET or not POST, return the current form
        return render(request, 'pages/confirm_delete.html', {'event': event})


def contact_view(request: HttpRequest) -> HttpRequest:
    """
    Handles contact form submissions.

    On a POST request, it saves the user's input from the contact form
    to the ContactMessage database. On a GET request, it displays a blank form.

    :param request: The HTTP request object (GET or POST).

    :type request: HttpRequest

    :returns: Redirects to the display_message page on successful submission,
              otherwise renders the 'contact.html' template with the form.

    :rtype: HttpRequest
    """
    # get form input
    if request.method == 'POST':
        # Bind user input
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            return redirect('planner:display_message', pk=contact_message.pk)
    else:
        form = ContactForm()
    # In case of a GET or error, return a blank form.
    return render(request, 'pages/contact.html', {'form': form})


def display_message(request: HttpRequest, pk: int) -> HttpRequest:
    """
    Displays the contents of a submitted contact message.

    Retrieves a ContactMessage instance based on its primary key (pk).

    :param request: The HTTP request object.

    :type request: HttpRequest

    :param pk: The primary key of the ContactMessage instance to display.

    :type pk: int

    :returns: Renders the 'messages.html' template, displaying the message.

    :rtype: HttpRequest
    """
    message = get_object_or_404(ContactMessage, pk=pk)
    return render(request, 'pages/messages.html', {'message': message})


def conditions_view(request: HttpRequest) -> HttpRequest:
    """
    Displays the terms and conditions of use.

    :param request: The HTTP request object.

    :type request: HttpRequest

    :returns: Renders the 'conditions.html' template, displaying
     the conditions.
    :rtype: HttpRequest
    """
    return render(request, 'pages/conditions.html')
