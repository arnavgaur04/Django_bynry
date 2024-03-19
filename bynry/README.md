
# BYNRY PROJECT

This is a Django application that provides consumers a way to generate service request.

### Using the project

```bash
git clone https://github.com/arnavgaur04/Django_bynry
cd bynry
```

```bash
python3 manage.py makemigrations members
```

```bash
python3 manage.py migrate
```

```bash
python3 manage.py runserver
```

### Dependencies

- Pillow
- Whitenoise

### Features

- Service requests: Users can request services.
- Request tracking: Users can see the details of their requests after submitting them.

### Structure of the project

#### Directory Structure:

    - bynry
        - media: contains files that are uploaded.

    - members
        - static: contains static files like .css files.

        - templates: contains .html files.
            - registration: contains login page .html.

    - mystaticfiles: global .css file is added here.
    
    - productionfiles: Django puts all the static files here.


