import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Project, Skill, Experience, ContactMessage
from django.contrib.auth.models import User

def seed_database():
    print("[+] Seeding Django Database for Jyotsana Runthla...")

    # 1. Create Superuser for Django Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'jyotsana.runthla@srmist.edu.in', 'admin123')
        print("  [OK] Superuser created -> Username: 'admin', Password: 'admin123'")
    else:
        print("  [INFO] Superuser 'admin' already exists.")

    # 2. Populate Projects
    Project.objects.all().delete()
    projects_data = [
        {
            'title': 'Big Data Predictive Analytics & Stream Engine',
            'summary': 'Distributed data stream pipeline analyzing massive datasets with real-time anomaly detection.',
            'description': 'Engineered using PySpark, Hadoop, and Django 6. Processes high-volume continuous data streams, performs predictive analytics modeling, and visualizes insights on an interactive dark-themed web dashboard.',
            'category': 'AI',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop',
            'github_url': 'https://github.com/jyotsanarunthla/big-data-analytics',
            'live_demo_url': 'https://demo.example.com/big-data',
            'technologies': 'Python, PySpark, Django, SQLite, Pandas, NumPy, Scikit-Learn',
            'featured': True,
        },
        {
            'title': 'Django Database Interactive Portfolio & Admin Portal',
            'summary': 'Modern glassmorphic portfolio web app with dynamic SQLite database model interactions and admin controls.',
            'description': 'Built for study purposes showcasing Django ORM model relationships, CSRF-protected form submissions, responsive glassmorphism CSS, and customizable Django Admin management interface.',
            'category': 'Web',
            'image_url': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop',
            'github_url': 'https://github.com/jyotsanarunthla/django-portfolio',
            'live_demo_url': 'https://demo.example.com/django-portfolio',
            'technologies': 'Python, Django, SQLite3, HTML5, Vanilla CSS3, JavaScript',
            'featured': True,
        },
        {
            'title': 'Healthcare Sentiment & Sentiment Analytics Platform',
            'summary': 'Natural Language Processing pipeline analyzing patient feedback using Big Data text mining algorithms.',
            'description': 'Processes customer reviews and medical telemetry text using NLTK and SpaCy. Provides aggregated metrics dashboards with CSV export and real-time query parameters via Django REST APIs.',
            'category': 'AI',
            'image_url': 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop',
            'github_url': 'https://github.com/jyotsanarunthla/sentiment-analytics',
            'live_demo_url': '',
            'technologies': 'Python, NLTK, Django, Pandas, SQLite, Chart.js',
            'featured': True,
        },
        {
            'title': 'Cloud Metrics & SQL Database Optimizer',
            'summary': 'DevOps tool for monitoring SQL query latency, database indexing bottlenecks, and server telemetry.',
            'description': 'Monitors database query execution times, flags missing indexes, and alerts developers to sub-optimal queries in SQLite and PostgreSQL databases.',
            'category': 'DevOps',
            'image_url': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop',
            'github_url': 'https://github.com/jyotsanarunthla/db-optimizer',
            'live_demo_url': '',
            'technologies': 'Python, Django, SQLite3, PostgreSQL, Docker',
            'featured': False,
        },
    ]

    for p in projects_data:
        Project.objects.create(**p)
    print(f"  [OK] Created {len(projects_data)} Projects.")

    # 3. Populate Skills
    Skill.objects.all().delete()
    skills_data = [
        {'name': 'Python 3', 'category': 'Backend', 'proficiency': 95, 'order': 1},
        {'name': 'Django & Django ORM', 'category': 'Backend', 'proficiency': 92, 'order': 2},
        {'name': 'REST API Architecture', 'category': 'Backend', 'proficiency': 88, 'order': 3},
        
        {'name': 'PySpark & Big Data Ecosystem', 'category': 'Database', 'proficiency': 90, 'order': 1},
        {'name': 'SQLite3, MySQL & SQL Queries', 'category': 'Database', 'proficiency': 92, 'order': 2},
        {'name': 'Pandas, NumPy & Data Wrangling', 'category': 'Database', 'proficiency': 94, 'order': 3},
        
        {'name': 'HTML5 & Vanilla CSS3', 'category': 'Frontend', 'proficiency': 90, 'order': 1},
        {'name': 'JavaScript (ES6+)', 'category': 'Frontend', 'proficiency': 85, 'order': 2},
        {'name': 'Responsive Glassmorphism UI', 'category': 'Frontend', 'proficiency': 88, 'order': 3},

        {'name': 'Git & GitHub Version Control', 'category': 'Tools', 'proficiency': 90, 'order': 1},
        {'name': 'Data Visualization (Matplotlib / Chart.js)', 'category': 'Tools', 'proficiency': 88, 'order': 2},
        {'name': 'Linux Shell & Command Line', 'category': 'Tools', 'proficiency': 85, 'order': 3},
    ]

    for s in skills_data:
        Skill.objects.create(**s)
    print(f"  [OK] Created {len(skills_data)} Skills.")

    # 4. Populate Experience & Education (Only SRM University B.Tech 2025 - Present)
    Experience.objects.all().delete()
    exp_data = [
        {
            'title': 'B.Tech in Big Data Analytics',
            'organization': 'SRM University, Chennai, Tamil Nadu',
            'type': 'education',
            'start_date': '2025',
            'end_date': 'Present',
            'description': 'Pursuing B.Tech in Big Data Analytics at SRM University, Chennai, Tamil Nadu.',
            'is_current': True,
            'order': 1
        },
    ]

    for e in exp_data:
        Experience.objects.create(**e)
    print(f"  [OK] Created {len(exp_data)} Education record.")


    # 5. Populate Initial Contact Message
    ContactMessage.objects.all().delete()
    ContactMessage.objects.create(
        name="SRM University Reviewer",
        email="student@srmist.edu.in",
        subject="Django Portfolio & Database Project Review",
        message="Hello Jyotsana! This portfolio project successfully demonstrates Django ORM models, database interaction, clean UI design, and Big Data specialization."
    )
    print("  [OK] Created sample ContactMessage entry.")

    print("[SUCCESS] Database seeding for Jyotsana Runthla completed successfully!")


if __name__ == '__main__':
    seed_database()
