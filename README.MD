# MailGram - MailService Project

MailGram is a robust email marketing platform built with Django, Django Rest Framework (DRF), PostgreSQL, Jinja, and Celery. It aims to provide a feature-rich environment for managing and sending marketing emails similar to popular services like Mailchimp.

## Features

- **User Authentication**: Secure user authentication system for account management.
- **Email Templates**: Create and manage customizable email templates using Jinja for dynamic content.
- **List Management**: Organize your audience with list management features.
- **Campaigns**: Schedule and send email campaigns to targeted lists.
- **Analytics**: Track email performance with analytics on open rates, click-through rates, etc. # TODO
- **Asynchronous Processing**: Use Celery for background tasks, ensuring efficient processing of email sending.

## Tech Stack

- **Python**: The core programming language.
- **Django**: The web framework for building the application.
- **Django Rest Framework (DRF)**: For building the RESTful APIs.
- **PostgreSQL**: The relational database for data storage.
- **Jinja**: Template engine for dynamic email content.
- **Celery**: Distributed task queue for asynchronous processing.


## Getting Started

1. **Clone the repository:**

   git clone https://github.com/isanjaymaurya/mailgram-webservice.git
   cd mailgram-webservice


## Setup Virtual Environment:

`python -m venv venv`
`source venv/bin/activate`   # For Linux/Mac
# OR
`.\venv\Scripts\activate`    # For Windows

## Install Dependencies:

`pip install -r requirements.txt`


## Run Migrations:

`python manage.py migrate`


## Run Development Server:

python manage.py runserver
The application will be accessible at `http://localhost:8000`.

## Run Celery Worker (in a separate terminal):

`celery -A mailservice worker -l info`