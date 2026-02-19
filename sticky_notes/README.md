# Sticky Notes – Django Practical Task

## 📌 Project Overview

This project is a **Sticky Notes Task Manager** developed using the Django framework.

The application allows users to:

- Create sticky notes
- View all notes
- Edit existing notes
- Delete notes
- Manage notes through a simple web interface

This project was completed as part of the practical assessment and includes:

- Django application source code
- Unit tests
- Design diagrams
- SQLite database
- Documentation for setup and usage

---

## 🎯 Objectives

The purpose of this task is to demonstrate:

- Django project structure
- CRUD operations (Create, Read, Update, Delete)
- Model–View–Template (MVT) architecture
- Unit testing in Django
- Basic software design documentation

---

## 🧱 Technologies Used

- Python 3.x
- Django
- SQLite3 (default Django database)
- HTML Templates

---

## 📂 Project Structure

```text
Django task/
│
├── diagrams/
│ ├── use_case_diagram.png
│ ├── architecture_diagram.png
│ └── erd_diagram.png
│
├── sticky_notes_project/
│ │
│ ├── manage.py
│ ├── requirements.txt
│ ├── README.md
│ │
│ ├── sticky_notes_project/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ │
│ └── notes/
│ ├── migrations/
│ ├── templates/
│ ├── tests.py
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── admin.py
│
└── sticky_github.txt
```

## 🚀 Getting Started
To run the project locally, follow these steps:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd sticky_notes_project
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.
---

