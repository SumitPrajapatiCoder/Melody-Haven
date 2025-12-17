# 🎵 MelodyHaven: Music Streaming Platform 🎵

MelodyHaven is a web application built with Django that allows users to upload, manage, and listen to their favorite music. It provides user authentication, song management, search functionality, and a clean, intuitive interface. Whether you're a music enthusiast or a budding artist, MelodyHaven offers a platform to share and enjoy music seamlessly.

## 🚀 Key Features

- **User Authentication:** Secure user registration, login, and logout functionality. 🔐
- **Song Management:** Upload, edit, and delete songs with ease. 🎶
- **Audio Playback:** Stream uploaded songs directly from the web interface. 🎧
- **Search Functionality:** Quickly find songs by title or artist. 🔍
- **Pagination:** Browse through large music libraries with efficient pagination. 📄
- **Admin Interface:** Django's built-in admin panel for managing users and songs. ⚙️
- **File Hash Check:** Prevents duplicate song uploads. ✅

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Django
- **Database:** SQLite (default, configurable)
- **Development Tools:** pip, Django CLI
- **Other:** Django Authentication, Django Forms, Django Templates

## 📦 Getting Started

### Prerequisites

- Python 3.7+ installed
- pip package installer
- Basic knowledge of Django framework

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd MelodyHaven
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```

### Running Locally

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Open your web browser and navigate to `http://127.0.0.1:8000/`**

## 📂 Project Structure

```
MelodyHaven/
├── manage.py               # Django's command-line utility
├── MelodyHaven/            # Project's main package
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL configuration
│   ├── asgi.py             # ASGI configuration for deployment
│   └── wsgi.py             # WSGI configuration for deployment
├── music/                # Django app for music management
│   ├── __init__.py
│   ├── admin.py            # Admin interface configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL configuration
│   ├── forms.py            # Django forms
│   ├── migrations/         # Database migrations
│   │   └── ...
│   └── templates/          # HTML templates
│       └── music/
│           └── ...
├── static/               # Static files (CSS, JavaScript, images)
│   └── ...
├── media/                # User-uploaded media files
│   └── ...
├── requirements.txt        # Project dependencies
└── db.sqlite3              # SQLite database (default)
```

## 📸 Screenshots

<img width="448" height="487" alt="image" src="https://github.com/user-attachments/assets/753c3d9c-002d-4f83-812f-6ec233ebe022" />

<img width="428" height="422" alt="image" src="https://github.com/user-attachments/assets/96bfe4b7-69af-4edf-b845-c4cda984b820" />

<img width="450" height="518" alt="image" src="https://github.com/user-attachments/assets/0c399c4e-8121-48d3-98dd-c4e00de694d1" />

<img width="1344" height="574" alt="image" src="https://github.com/user-attachments/assets/6fcfd186-8ed9-43e1-bf53-31ca6ed62e18" />

<img width="449" height="415" alt="image" src="https://github.com/user-attachments/assets/34807854-e456-44a1-9355-9abf120d518a" />

<img width="1361" height="465" alt="image" src="https://github.com/user-attachments/assets/b46a5cfe-e289-4d2f-a042-89c42b55024f" />

<img width="1357" height="566" alt="image" src="https://github.com/user-attachments/assets/cf2f3875-2590-451b-9c65-b261b95dc4f5" />








This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
