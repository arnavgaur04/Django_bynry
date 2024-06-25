
# BYNRY PROJECT

This is a Django application that provides consumers a way to generate service request.

### Using the project

```bash
git clone https://github.com/arnavgaur04/DjangoBasedApp
cd app
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

    - app
        - media: contains files that are uploaded.

    - members
        - static: contains static files like .css files.

        - templates: contains .html files.
            - registration: contains login page .html.

    - mystaticfiles: global .css file is added here.
    
    - productionfiles: Django puts all the static files here.





#### Credentials:

1. user1:
    - username: user1
    - password: personuser1

2. user2:
    - username: user2
    - password: personuser2

3. user3:
    - username: user3
    - password: personuser3

4. admin:
    - username: admin
    - password: admin1234
