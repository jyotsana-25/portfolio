from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Project, Skill, Experience, ContactMessage
from .forms import ContactForm


def index(request):
    """
    Main Portfolio Homepage view.
    Retrieves database objects for projects, skills, and experiences.
    Processes Contact Form submissions.
    """
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves directly into SQLite database via ContactMessage model!
            messages.success(request, "🎉 Your message has been sent successfully! I will get back to you soon.")
            return redirect('portfolio:index')
        else:
            messages.error(request, "⚠️ Please correct the errors in the form below.")

    # Database Queries using Django ORM
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    
    # Categorize skills for clean layout rendering
    skills_by_category = {
        'Frontend': Skill.objects.filter(category='Frontend'),
        'Backend': Skill.objects.filter(category='Backend'),
        'Database': Skill.objects.filter(category='Database'),
        'Tools': Skill.objects.filter(category='Tools'),
    }

    work_experiences = Experience.objects.filter(type='work')
    education = Experience.objects.filter(type='education')

    # Total counts for statistics counter bar
    stats = {
        'projects_count': projects.count(),
        'skills_count': Skill.objects.count(),
        'messages_count': ContactMessage.objects.count(),
    }

    context = {
        'projects': projects,
        'featured_projects': featured_projects,
        'skills_by_category': skills_by_category,
        'work_experiences': work_experiences,
        'education': education,
        'form': form,
        'stats': stats,
    }
    return render(request, 'portfolio/index.html', context)


def project_detail(request, slug):
    """
    Detail View for single project showcase.
    Queries database for project slug, and fetches related projects.
    """
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]

    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)
