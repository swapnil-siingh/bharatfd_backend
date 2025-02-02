# Django FAQ Application with Multilingual Support for BharatFD Backend Role

## Overview
This is a Django-based FAQ (Frequently Asked Questions) application that supports multiple languages using Google Translate. The application allows users to view FAQs, switch languages dynamically, and provides an admin panel for managing FAQs.

## Features
- View FAQs in multiple languages (English, Hindi, Bengali, French, etc.).
- Auto-translate questions/answers using Google Translate API.
- Admin panel to add, edit, and delete FAQs.
- Uses Django REST Framework (DRF) for API-based access.
- Caching for optimized performance.

##Screenshots
![bharatfdscreenshot](https://github.com/user-attachments/assets/61909944-e41b-499b-9c13-958bae2a4800)


## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS (Tailwind), 
- **Database**: SQLite (default)
- **Caching**: Django Cache
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

### 7. The application will be available at `http://127.0.0.1:8000/`.
#For Login Dummy Users

##FOR ADMIN: username - root || Passoword - 1234
##FOR OTHERS: username - dummy || Password - Bharat@1234


#(optional) Install Redis(if not installed already) using Chocolatey


## Step 1: Open PowerShell as Administrator
1. Run the following command to allow script execution:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   ```

## Step 2: Install Chocolatey
Run the following command in PowerShell:
```powershell
iwr https://community.chocolatey.org/install.ps1 -UseBasicParsing | iex
```
Wait for the installation to complete.

## Step 3: Verify Chocolatey Installation
Close and reopen PowerShell, then run:
```powershell
choco -v
```
If installed correctly, it will display the version number.

## Step 4: Install Redis
Now, install Redis using Chocolatey:
```powershell
choco install redis -y
```

## Step 5: Start Redis
To start Redis manually, run:
```powershell
redis-server
```


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
$ python manage.py migrate
```

