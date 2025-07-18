```markdown
# __django

A simple Django-based web application demonstrating basic project structure, user authentication, and article management. This is a beginner-friendly project ideal for learning Django’s MVC architecture, templates, forms, and admin interface.

---

## 🔧 Tech Stack

- **Backend:** Django 3.2+
- **Frontend:** HTML (Django Templates)
- **Database:** SQLite (default Django DB)
- **Language:** Python 3.8

---

## 📁 Project Structure

```

__django/
├── accounts/ # Handles user registration and login
├── articles/ # Article model, views, and forms
├── templates/ # Global templates (base.html, etc.)
├── .venv/ # Virtual environment (not tracked)
├── db.sqlite3 # Default database
├── manage.py # Django project management tool
└── static/ # Static files (CSS, JS, images)

````

---

## 🚀 Features

- User registration and login system
- Article CRUD operations
- Django Admin for content management
- Modular app structure
- Clean and customizable templates

---

## ✅ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pewpiece/__django.git
cd __django
````

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, manually install:
>
> ```bash
> pip install django
> ```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧪 Tests

Basic testing can be run via:

```bash
python manage.py test
```

---

## 🛠 Future Improvements

* Add REST API with Django REST Framework
* Implement pagination and search for articles
* Add user profile page
* Add social login via OAuth

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Pewpiece**
GitHub: [@pewpiece](https://github.com/pewpiece)