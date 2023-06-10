# Blogging App

This is an Blogging Concept created using Django Web Framework.


## Features

* Create Blog Account
* Account Signin and Singout
* Like and dislike posts
* Add comments
* Upload a Post in the blog

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Git
+ pip

## Requirements

+ Django==4.0.1
+ python-dateutil==2.8.2

## Project Installation
```
cd ablog
```
Migrate Database,
```bash
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```

Admin Username,
```bash
Username: admin
Password: 1234
```
