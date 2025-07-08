from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

# Create your views here.


def accounts_index(request: HttpRequest) -> HttpRequest:
    """
    Accesses request object data for the profile page.

    :param request: The HTTP request object.

    :type request: HttpRequest

    :returns: An HTTP response object that will eventually render the
     profile page.

    :rtype: HttpRequest
    """
    return HttpResponse('<h2>This will become the profile page</h2>')


def user_login(request: HttpRequest) -> HttpRequest:
    """
    Handles user login requests.

    :param request: The HTTP request object, containing login data if POST.

    :type request: HttpRequest

    :returns: Renders the login page HTML.

    :rtype: HttpRequest
    """
    return render(request, 'authentication/login.html')


def register(request: HttpRequest) -> HttpRequest:
    """
    Handles user registration requests.

    Processes the registration form, saves user details, and renders
    the signup HTML form.

    :param request: The HTTP request object, containing
     registration form data if POST.

    :type request: HttpRequest

    :returns: Redirects to the login page on successful registration,
              otherwise renders the signup form with errors.

    :rtype: HttpRequest
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("Form errors:", form.errors)
        if form.is_valid():
            # Set Password
            user = form.save(commit=False)
            # Clean Inputs
            user.set_password(form.cleaned_data['password1'])
            # Save Form Input
            form.save()
            # Conditionally log user in if required, or redirect:
            # login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'authentication/register.html', {'form': form})


def authenticate_user(request: HttpRequest) -> HttpRequest:
    """
    Authenticates user data submitted via the login page.

    :param request: The HTTP request object, containing user
     login data if POST.

    :type request: HttpRequest

    :returns: Redirects to the planner index on successful authentication,
              otherwise re-renders the login page with errors.

    :rtype: HttpRequest
    """
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        # Bind POST data to the form
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Authentication successful
                login(request, user)
                # Redirect to your schedule view after successful login
                return redirect('planner:index')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        # This block handles GET requests (initial page load for the form)
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {"form": form})


def logout_view(request: HttpRequest) -> HttpRequest:
    """
    Handles user logout requests.

    :param request: The HTTP request object.

    :type request: HttpRequest

    :returns: Redirects the user to the login page after logging out.

    :rtype: HttpRequest
    """
    logout(request)
    return redirect('accounts:login')

# Unused view for now. Will turn into profile view next


def show_user(request: HttpRequest) -> HttpRequest:
    """
    Displays details for the logged-in user.

    :param request: The HTTP request object, containing logged-in user details.

    :type request: HttpRequest

    :returns: Renders HTML with the user's profile view.

    :rtype: HttpRequest
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
