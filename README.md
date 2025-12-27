# Django Learning Project - Blog Application

A comprehensive Django project created for learning Django framework step by step. This repository demonstrates various Django concepts and features through building a blog application.

## 📚 Learning Topics Covered

This project covers the following Django topics:

1. **Installing Django & Course Setup** - Project initialization and environment setup
2. **URLs & Views** - Routing and request handling
3. **Templates, Context Processors & Static Files** - Frontend templating and asset management
4. **Databases, ORM & Models** - Database design and Object-Relational Mapping
5. **Admin & ModelAdmin** - Django admin interface customization
6. **Working with Forms & ModelForms** - Form handling and validation
7. **Cookies in Django** - Managing client-side data storage
8. **Middlewares in Django** - Request/response processing
9. **Working with Sessions** - Server-side session management
10. **Authentication & Authorization** - User management and permissions
11. **Pagination** - Splitting data across multiple pages
12. **Relationships in Django** - Model relationships (One-to-One, One-to-Many, Many-to-Many)
13. **Handling File Uploads & Images** - Media file management
14. **Adding More Features** - Extended functionality
15. **Deep Dive into Class-Based Views** - Advanced view patterns

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- Docker (optional)

### Installation

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
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
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

Visit `http://127.0.0.1:8000` to see the application.

### Using Docker

Alternatively, you can run the project using Docker:

```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`.

## 📂 Project Structure

```
blog/
├── blog/           # Main project configuration
├── posts/          # Blog posts application
├── manage.py       # Django management script
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## 🛠️ Technologies Used

- Django 6.x
- Python 3.14
- SQLite (development)
- Docker

## 📝 License

This project is created for educational purposes.

## 🎯 Purpose

This repository serves as a hands-on learning resource for mastering Django web framework, progressively implementing features from basic to advanced concepts.
