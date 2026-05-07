# Django Learning Project - Blog Application

A comprehensive Django project built to learn the Django framework step by step. This repository demonstrates core Django concepts by developing a blog application.

---

## 📚 Learning Topics Covered

This project covers the following Django topics:

1. **Installing Django & Project Setup (Docker)** – Project initialization and environment setup **(Completed)**

   * Setting up a Django project using Docker for containerization and easier deployment

2. **URLs & Views** – Routing and request handling **(Completed)**

3. **Templates, Context Processors & Static Files** – Frontend templating and asset management **(Completed)**

4. **Databases, ORM & Models** – Database design and Object-Relational Mapping **(Ongoing)**

5. **Admin & ModelAdmin** – Django admin interface customization

6. **Forms & ModelForms** – Form handling and validation

7. **Cookies in Django** – Managing client-side data

8. **Middleware in Django** – Request/response lifecycle processing

9. **Sessions** – Server-side session management

10. **Authentication & Authorization** – User management and permissions

11. **Pagination** – Handling large datasets across multiple pages

12. **Model Relationships** – One-to-One, One-to-Many, Many-to-Many

13. **File Uploads & Images** – Media handling

14. **Feature Extensions** – Adding additional functionality

15. **Class-Based Views (CBVs)** – Advanced view patterns

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* pip
* Docker (optional)

---

## ⚙️ Installation (Without Docker)

1. Clone the repository:

```bash
git clone <repository-url>
cd blog
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

👉 Visit: `http://127.0.0.1:8000`

---

## 🐳 Using Docker

Run the project with Docker:

```bash
docker compose up --build
```

👉 The application will be available at: `http://localhost:8000`

### Running Migrations in Docker

To create and apply migrations inside the Docker container:

```bash
# Start the container in detached mode first
docker compose up -d

# Create migration files
docker compose exec web python manage.py makemigrations

# Apply migrations to the database
docker compose exec web python manage.py migrate

# Create a superuser (optional)
docker compose exec web python manage.py createsuperuser
```

---

## � Common Django Commands

### Creating a New App

To create a new Django application:

**Without Docker:**
```bash
python manage.py startapp <app_name>
```

**With Docker:**
```bash
docker compose exec web python manage.py startapp <app_name>
```

After creating an app, add it to the `INSTALLED_APPS` list in `blog/settings.py`.

### Managing Migrations

**Without Docker:**
```bash
# Create migration files based on model changes
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Show all migrations and their status
python manage.py showmigrations

# Show migrations for a specific app
python manage.py showmigrations <app_name>

# Apply migrations for a specific app
python manage.py migrate <app_name>

# Unapply migrations (rollback)
python manage.py migrate <app_name> <migration_number>
```

**With Docker:**
```bash
# Create migration files based on model changes
docker compose exec web python manage.py makemigrations

# Apply migrations to the database
docker compose exec web python manage.py migrate

# Show all migrations and their status
docker compose exec web python manage.py showmigrations

# Show migrations for a specific app
docker compose exec web python manage.py showmigrations <app_name>

# Apply migrations for a specific app
docker compose exec web python manage.py migrate <app_name>

# Unapply migrations (rollback)
docker compose exec web python manage.py migrate <app_name> <migration_number>
```

### Other Useful Commands

**Without Docker:**
```bash
# Create a superuser for admin access
python manage.py createsuperuser

# Open Django shell for interactive testing
python manage.py shell

# Collect static files
python manage.py collectstatic
```

**With Docker:**
```bash
# Create a superuser for admin access
docker compose exec web python manage.py createsuperuser

# Open Django shell for interactive testing
docker compose exec web python manage.py shell

# Collect static files
docker compose exec web python manage.py collectstatic
```

---

## �📂 Project Structure

```
.
├── blog/                   # Project configuration
│   ├── context_processors.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── posts/                  # Blog application
│   ├── management/         # Custom management commands
│   ├── migrations/         # Database migrations
│   ├── templates/          # App-specific templates
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── static/                 # Static files (CSS, JS, images)
│   └── css/
├── templates/              # Global templates
│   ├── partials/           # Reusable components
│   ├── 404.html
│   └── base.html
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

* Django 6.x
* Python 3.x
* SQLite (development)
* Docker

---

## 🎯 Purpose

This repository serves as a hands-on learning resource for mastering the Django web framework, progressively building from basic to advanced concepts through practical implementation.

---

## 📝 License

This project is intended for educational purposes only.