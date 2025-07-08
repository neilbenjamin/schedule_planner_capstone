# Build solution courtesy of Google.
# Use a Python base image. It's good practice to be specific with version.
FROM python:3.11-slim-bookworm

# Set the initial directory where all run and copy commands will take place
# relative the WORKDIR, unless a new WORKDIR is specified
WORKDIR /app

# Installs all the system necessary dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    # Add any other system dependencies you might need, e.g., for image processing:
    # libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project source code into the container's /app directory.
# The .dockerignore file (placed in '/') will prevent unnecessary files.
COPY . /app/

# Change the working directory to your Django project root inside the container.
# This is where manage.py is located.
# Based on your structure: /app/schedule_planner/
WORKDIR /app/schedule_planner 

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=schedule_planner.settings 

# Run Django migrations
RUN python manage.py migrate --noinput

# Collect static files
RUN python manage.py collectstatic --noinput

# Create port that Gunicorn (or Django's runserver) will listen on
EXPOSE 8000

# Command to run your Django application using Gunicorn
# schedule_planner.wsgi:application refers to the wsgi.py file inside your
# inner 'schedule_planner' directory (e.g., /app/schedule_planner/schedule_planner/wsgi.py)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "schedule_planner.wsgi:application"]