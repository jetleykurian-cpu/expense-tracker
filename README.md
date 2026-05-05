# Expense Tracker

A full stack web application built with Python and Django.

## Features
- User registration and login
- Each user sees only their own expenses
- Add expenses with name, amount, category and notes
- Live total calculated automatically
- Data persisted in SQLite database

## Tech Stack
- Python 3.13
- Django 6.0
- SQLite

## How to run locally
```bash
# clone the repo
git clone https://github.com/jetleykurian-cpu/expense-tracker.git
cd expense-tracker

# create and activate virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# install dependencies
pip install django

# run migrations
python manage.py migrate

# create admin user
python manage.py createsuperuser

# start server
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## What I learned building this
- Django project structure (models, views, urls, templates)
- ORM — database queries without SQL
- ModelForm — forms tied directly to database models
- Django authentication — login, logout, register
- User-specific data filtering