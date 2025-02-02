# Django FAQ Application with Multilingual Support

## Overview
This is a Django-based FAQ (Frequently Asked Questions) application that supports multiple languages using Google Translate. The application allows users to view FAQs, switch languages dynamically, and provides an admin panel for managing FAQs.

## Features
- View FAQs in multiple languages (English, Hindi, Bengali, French, etc.).
- Auto-translate questions using Google Translate API.
- Admin panel to add, edit, and delete FAQs.
- Uses Django REST Framework (DRF) for API-based access.
- Caching for optimized performance.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **Database**: SQLite (default) / PostgreSQL (recommended for production)
- **Caching**: Django Cache (Redis recommended for better performance)
- **Translation**: Google Translate API

## Installation
### 1. Clone the Repository
```sh
$ git clone https://github.com/your-repo/django-faq-app.git
$ cd django-faq-app
```

### 2. Create a Virtual Environment & Activate It
```sh
$ python -m venv venv
$ source venv/bin/activate  # On macOS/Linux
$ venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
$ python manage.py migrate
```

### 5. Create a Superuser (For Admin Access)
```sh
$ python manage.py createsuperuser
```
Follow the prompts to set up an admin username and password.

### 6. Run the Server
```sh
$ python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Usage
### **Homepage**
- Displays a dropdown menu to select a language.
- Shows FAQs in the selected language.
- Admin users can edit or delete FAQs.

### **Admin Panel**
- Access the Django Admin at `http://127.0.0.1:8000/admin/`.
- Log in with your superuser credentials.
- Add, edit, or delete FAQs.

### **API Endpoints**
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| GET    | `/api/faqs/`    | Get all FAQs |
| GET    | `/api/faqs/?lang=fr` | Get FAQs in French |
| POST   | `/api/faqs/`    | Create a new FAQ |
| PUT    | `/api/faqs/{id}/` | Update an FAQ |
| DELETE | `/api/faqs/{id}/` | Delete an FAQ |

## Configuration
### 1. **Adding More Languages**
To add more languages, modify the `FAQ` model in `models.py`:
```python
target_languages = ['hi', 'bn', 'fr', 'es']  # Add new languages here
```

### 2. **Changing Database**
To use PostgreSQL, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'faq_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Run migrations again:
```sh
$ python manage.py migrate
```

### 3. **Enable Caching (Redis Recommended)**
To improve performance, configure Django caching in `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

