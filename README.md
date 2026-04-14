# 🎬 Netflix Tudum — Django Web Application

A Netflix-inspired web application built with Django, featuring a multi-page layout with user authentication, registration, and content pages styled with Bootstrap 5.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Development Server](#running-the-development-server)
- [URL Routes](#url-routes)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## About the Project

**Netflix Tudum** is a Django-based web application that replicates the look and feel of Netflix's landing experience. It includes a home page, an about page, a contact page, a form page, and a full user authentication flow (login & registration) using Django's built-in auth system.

---

## Features

- 🏠 Landing / Home page
- 🔐 User Login with Django authentication
- 📝 User Registration page
- ℹ️ About page
- 📬 Contact page
- 📋 Form page
- 🎨 Bootstrap 5 for responsive styling
- 🗄️ SQLite3 database (development)
- ☁️ Deployment-ready with Gunicorn + Procfile

---

## Tech Stack

| Layer      | Technology                  |
|------------|-----------------------------|
| Backend    | Python, Django 6.0.1        |
| Frontend   | HTML5, CSS3, Bootstrap 5    |
| Database   | SQLite3                     |
| Server     | Gunicorn (production)       |
| Deployment | Heroku (via Procfile)       |

---

## Project Structure

```
Netflix_Tudum/
│
├── config/                  # Django project configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI entry point
│   └── asgi.py              # ASGI entry point
│
├── home/                    # Main Django app
│   ├── templates/           # HTML templates
│   │   ├── index.html       # Main landing page
│   │   ├── Home.html        # Home page (authenticated)
│   │   ├── Login.html       # Login page
│   │   ├── Register.html    # Registration page
│   │   ├── About.html       # About page
│   │   ├── Contact.html     # Contact page
│   │   └── form.html        # Form page
│   ├── static/
│   │   ├── css/             # Bootstrap 5 + custom styles
│   │   └── js/              # Bootstrap 5 JS bundles
│   ├── views.py             # View functions
│   ├── urls.py              # App-level URL patterns
│   ├── models.py            # Database models
│   └── admin.py             # Django admin config
│
├── manage.py                # Django management utility
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku deployment config
└── db.sqlite3               # SQLite database (dev only)
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Arjunkalliyadath/django-project1.git
   cd django-project1
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **(Optional) Create a superuser for Django admin:**

   ```bash
   python manage.py createsuperuser
   ```

### Running the Development Server

```bash
python manage.py runserver
```

Open your browser and go to: **http://127.0.0.1:8000/**

---

## URL Routes

| URL            | View            | Description              |
|----------------|-----------------|--------------------------|
| `/`            | `home`          | Main landing page        |
| `/home/`       | `home_page`     | Home page (post-login)   |
| `/login/`      | `login_view`    | User login               |
| `/register/`   | `register`      | User registration        |
| `/about/`      | `about`         | About page               |
| `/contact/`    | `contact`       | Contact page             |
| `/form/`       | `form_view`     | Form page                |
| `/admin/`      | Django Admin    | Admin dashboard          |

---

## Deployment

This project is configured for deployment on **Heroku** using Gunicorn.

The `Procfile` contains:
```
web: gunicorn config.wsgi
```

### Steps to deploy on Heroku:

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Login and create an app:
   ```bash
   heroku login
   heroku create your-app-name
   ```
3. Push to Heroku:
   ```bash
   git push heroku main
   ```
4. Run migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```

> **Note:** Before deploying to production, make sure to set `DEBUG = False` and configure a proper `SECRET_KEY` via environment variables. Do **not** commit your secret key to version control.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## Author

**Arjun Kalliyadath**  
GitHub: [@Arjunkalliyadath](https://github.com/Arjunkalliyadath)
