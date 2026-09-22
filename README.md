# 🎓 Django Portfolio Website - Jyotsana Runthla

A modern, database-driven **Django Web Application** featuring dynamic portfolio showcases, skill visualizers, education timeline, interactive contact form handling, and custom Django Admin panel.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.1-green?logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey?logo=sqlite)

---

## 🌟 Overview & Features

- **Personal Profile**: Customized for **Jyotsana Runthla**, B.Tech Big Data Analytics student at **SRM University, Chennai, Tamil Nadu**.
- **Django ORM Database Interaction**:
  - `Project`: Dynamic project items with category filter tabs and detailed showcase pages.
  - `Skill`: Interactive skill progress bars categorized by technology areas.
  - `Experience`: Academic background timeline highlighting SRM University degree (2025 – Present).
  - `ContactMessage`: CSRF-protected contact form saving incoming inquiries straight into the SQLite database.
- **Glassmorphism Aesthetic**: Modern dark UI with ambient gradient glows, CSS grid layouts, and micro-interactions.
- **Django Admin Panel**: Full database control at `/admin/`.
- **Database Seeder**: Automated setup via `seed_data.py`.

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/jyotsana-25/portfolio.git
cd portfolio
```

### 2. Install Dependencies
Ensure Python 3.10+ is installed, then install Django:
```bash
pip install django
```

### 3. Run Migrations & Seed Database
```bash
python manage.py migrate
python seed_data.py
```

### 4. Start Development Server
```bash
python manage.py runserver 8000
```
Open **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

## 🔐 Django Admin Credentials
Access the admin portal at **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**:
- **Username**: `admin`
- **Password**: `admin123`

---

## 📁 Project Structure

```
portfolio/
├── manage.py                     # Django CLI utility
├── seed_data.py                 # Database seeder script
├── portfolio_project/            # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                    # Main app directory
│   ├── models.py                # Project, Skill, Experience, ContactMessage
│   ├── views.py                 # Index & Project Detail view logic
│   ├── forms.py                 # ContactForm ModelForm definition
│   ├── admin.py                 # Django Admin configurations
│   └── templates/portfolio/     # DTL templates (base.html, index.html, detail.html)
└── static/                       # Static assets
    ├── css/style.css            # Dark mode glassmorphism styles
    └── js/main.js               # Category filtering & animation scripts
```
