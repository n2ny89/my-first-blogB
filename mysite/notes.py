"""
Django Notes

1) Install Python
2) Start virtual env
3) Install Django:
    pip install -r requirements.txt
4) Start Project
    django-admin.exe startproject mysite . 
        > the period in the end indicates "do not create a main folder"
5) Customize Settings File
    ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
        > indicates which urls is allowed to access the site files
    DATABASES
        > indicate which database will be used for the site
    LANGUAGE CODE
        > which language to use, for example "Americas/Los_Angeles"
    STATIC URLS - tells python how to look for static files
        > STATIC_URL = '/static/'
        > STATIC_ROOT = os.path.join(BASE_DIR, 'static')
6) SETUP/Initialize database
    Use manage.py to update database
        > py manage.py migrate
7) Confirm setup is successful
    Use manage.py to start the local server
        >py manage.py runserver
    Go to browser and access local server
        > 127.0.0.1:8000
8) Ceate Application
    Create an application for your website using manage.py
        > py manage.py startapp blog
    Register Apllication in Settings so Django Recognizes it
        > In the Settings File
            > Under 'Installed Apps' add:
                'blog.apps.BlogConfig'
9) Model
    Models are the objects in the application such as "posts", "users" ...
        > Objects have properties and methods
        > Models are saved in tables in the database
    In an app directory open models.py
        Import necessary modules
            > from django.conf import settings
            > from django.db import models
            > from django.utils import timezone
        Class anatomy:
            class Post(models.Model):
                    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
                    title = models.CharField(max_length=200)
                    text = models.TextField()
                    created_date = models.DateTimeField(default=timezone.now)
                    published_date = models.DateTimeField(blank=True, null=True)

                    def publish(self):
                        self.published_date = timezone.now()
                        self.save()

                    def __str__(self):
                        return self.title
    Update database with model changes
        Prepare model changes:
            > py manage.py makemigrations blog
        Apply model changes:
            > py manage.py migrate blog
10) Django Admin
        Django-admin is a built in admin interface

        Connect an Model/Object to the admin interface
            a) Edit admin file inside the app directory
                i. import necessary modules
                    > from django.contrib import admin
                    > from .models import Post

                ii. Add line to register app:
                    > admin.site.register(Post)

11) GIT
        GIT is a version control system
            1) Install GIT from website
            2) Using CMD go to project directory and enter:
                > git init
                > git config --global user.name "Your Name"
                > git config --global user.email you@example.com
            3) Create .gitignore file to ignore files that are unecessary/untransferrable
                In the base directory create a file title '.gitignore' and write:
                    *.pyc
                    *~
                    /.vscode
                    __pycache__
                    myvenv
                    db.sqlite3
                    /static
                    .DS_Store

         
    

