# Django Schedule Planner

Basic schedule planner to assist event coordinators with planning with entertainers and event crew over a given period of time. Admin users will have access to CRUD functionality while mid management will have access to the schedules.

## Table of contents
- [1. Features](#1-features)
- [2. How to Install](#2-how-to-install)
- [3. Environment Variables](#3-environment-variables)
- [4. App Operation](#4-app-operation)
- [5. Images](#5-images)
- [6. Deployment](#6-deployment)
- [7. License](#7-license)
- [8. Docker Usage](#8-docker-usage)
- [9. Building Documentation (Sphinx)](#9-building-documentation-sphinx)

## 1. Features

- Django 5.2.1
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with Render.
- PostgreSQL database in production mode and SQLite in development mode.
- Crispy Forms and Bootstrap for styling
- PostgreSQL database support with psycopg2.
- Whitenoise for managing static transfers

## 2. How to Install

### 🚀 Getting Started

Follow these steps to set up and run the project locally.

#### Prerequisites

* Python 3.x
* pip (Python package installer)

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/neilbenjamin/your-repo-name.git](https://github.com/neilbenjamin/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**

    It's highly recommended to use a virtual environment to manage project dependencies isolation.

    ```bash
    # Create the virtual environment (named '.venv' in this example)
    python3 -m venv .venv

    # Activate the virtual environment:
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows (Command Prompt):
    # .venv\Scripts\activate.bat
    # On Windows (PowerShell):
    # .venv\Scripts\Activate.ps1
    ```
    *Note: If you use a virtual environment manager like `virtualenvwrapper` or `pyenv-virtualenv`, you can use its equivalent commands (e.g., `mkvirtualenv your-project-name` and `workon your-project-name`) instead of the `venv` commands above.*

3.  **Install project dependencies:**
    With your virtual environment activated:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application should now be accessible at `http://127.0.0.1:8000/`.

## 3. Environment Variables

Your project is configured to use environment variables for sensitive data and deployment-specific settings. You will need to set these variables in your deployment environment (e.g., in the "Environment" section of your web service on the Render Dashboard).

#### Required Environment Variables:

* **`SECRET_KEY`**
    * **Purpose:** A unique, long, and random string used by Django for cryptographic signing (e.g., sessions, password resets). This is **critical for security** in production.
    * **Value to set:** A very long, randomly generated string.
    * **How to generate a new key:**
        ```bash
        python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
        ```
    * **Example (do NOT use this exact value for your deployed app):** `my-very-long-and-random-secret-key-123abc456def789ghi`
    * **Note:** Your `settings.py` includes a fallback hardcoded key for local development if this variable is not set. For production, **always set this environment variable.**

* **`DATABASE_URL`**
    * **Purpose:** The connection string for your PostgreSQL database. Your application uses `dj_database_url` to configure the database connection based on this string.
    * **Value to set:** A URL string in the format `postgres://user:password@host:port/dbname`.
    * **Note:** If you're using Render's managed PostgreSQL database, Render automatically provides this environment variable to your web service, so you typically don't need to set it manually.

* **`DJANGO_DEBUG`**
    * **Purpose:** Controls Django's `DEBUG` mode. When `DEBUG` is `True`, Django provides detailed error pages and certain development-only features. It should **always be `False` in production** for security.
    * **Value to set:** `True` or `False` (as string literals).
    * **Recommended for Production:** `False`
    * **Example:** `DJANGO_DEBUG='False'`

* **`ALLOWED_HOSTS`**
    * **Purpose:** A comma-separated list of hostnames (domain names or IP addresses) that your Django application is allowed to serve. This is a vital security measure to prevent HTTP Host header attacks.
    * **Value to set:** A comma-separated string of your application's domain(s).
    * **Example:** `ALLOWED_HOSTS='your-app-name.onrender.com,www.your-custom-domain.com'`
    * **Note:** Your `settings.py` is configured to automatically include Render's external hostname (`RENDER_EXTERNAL_HOSTNAME`) if it's available, so you might only need to set this for additional custom domains.

## 4. App Operation

-   Create an account
-   Log in
-   View schedule
-   Add, update, or delete entries
-   Contact Admin

## 5. Images

Here are some screenshots and visual aids for the Schedule Planner:

* **Dashboard View:**
    ![Dashboard View](schedule_planner/images/dashboard.png)

* **Add Event Page:**
    ![Add Event Page](schedule_planner/images/add_event.png)

* **Terms and Conditions:**
    ![Terms and Conditions](schedule_planner/images/conditions.png)

* **Contact Us Page:**
    ![Contact Us Page](schedule_planner/images/contact_us.png)

* **Delete Confirmation:**
    ![Delete Confirmation](schedule_planner/images/delete.png)

* **User Registration:**
    ![User Registration Page](schedule_planner/images/register.png)

## 6. Deployment

You can deploy to your choice of deployment options and based on those, you may need to reconfigure your settings to match the host deployment requirements.

## 7. License

Copyright (c) 2025 Neil Benjamin

Permission is restricted for any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

## Quick Links

-   [GitHub](https://github.com/neilbenjamin/01_schedule_planner/blob/main/README.md)

---

## 8. Docker Usage

This project includes a `Dockerfile` for containerizing the Django application, making it easy to build, ship, and run in various environments. The `Dockerfile` is located in the root directory of the project.

### Building the Docker Image

To build the Docker image for your application, navigate to the root directory of the project in your terminal (where the `Dockerfile` resides) and run:

```bash
docker build --platform linux/amd64 -t schedule-planner-app .
```
Be aware of what architechture you;re using as older machines won't be able to run the arm64 architechture. This bulid was done to emulate the linux/amd64 set up which is widely used for Render and Dockerplay. If you are running a new amr64 architecture machine, you may receive a warning stating that the build is meant for linux/amd64, but you can ignore 
that and navigate to your localhost:8000 and your app will be available, locally. For production, pleas refer to No. 6

## 9. Building Documentation (Sphinx)

This project's documentation is built using [Sphinx](https://www.sphinx-doc.org/en/master/). The source files for the documentation are located in the `schedule_planner/docs/` directory. The generated documentation (e.g., HTML files) is excluded from Git to keep the repository lean.

To build and view the documentation locally:

1.  **Prerequisites:**
    * Ensure you have Sphinx installed in your project's virtual environment. It's listed in `requirements.txt`, so it will be installed along with other dependencies during the standard installation:
        ```bash
        pip install -r requirements.txt
        ```
    * (Optional, but good practice): If you plan to build the docs, ensure your project's `schedule_planner` app is on your Python path, for example by running from the project root:
        ```bash
        export PYTHONPATH=$PYTHONPATH:$(pwd)
        ```

2.  **Navigate to the Documentation Source Directory:**
    ```bash
    cd schedule_planner/docs/
    ```

3.  **Build the HTML Documentation:**
    Run the Sphinx build command. This will generate the HTML files in the `_build/html` subdirectory within the `schedule_planner/docs/` folder.
    ```bash
    sphinx-build -b html . _build/html
    ```
    * `sphinx-build`: The Sphinx builder command.
    * `-b html`: Specifies that HTML output should be generated.
    * `.`: Indicates the source directory for the documentation (the current directory, `schedule_planner/docs/`).
    * `_build/html`: The target directory where the generated HTML files will be placed.

4.  **View the Documentation:**
    Once the build is complete, you can open the main `index.html` file in your web browser. From the `schedule_planner/docs/` directory:
    ```bash
    # On macOS:
    open _build/html/index.html
    # On Windows (Command Prompt):
    start _build/html/index.html
    # On Linux (various desktop environments):
    xdg-open _build/html/index.html
    # Alternatively, you can manually navigate to the file in your browser's file open dialog.
    ```