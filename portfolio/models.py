from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Web', 'Web Development'),
        ('AI', 'AI & Machine Learning'),
        ('Mobile', 'Mobile Applications'),
        ('DevOps', 'Cloud & DevOps'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=300, help_text="Short blurb for project cards")
    description = models.TextField(help_text="Detailed markdown or plain text description")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Web')
    image_url = models.URLField(
        default="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop",
        help_text="Direct link to project screenshot or thumbnail"
    )
    github_url = models.URLField(blank=True, help_text="GitHub Repository Link")
    live_demo_url = models.URLField(blank=True, help_text="Live Working Demo Link")
    technologies = models.CharField(
        max_length=250, 
        help_text="Comma-separated tech list, e.g. Python, Django, PostgreSQL, HTML5, CSS3"
    )
    featured = models.BooleanField(default=False, help_text="Show in featured section")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def tech_list(self):
        """Returns a list of trimmed technology strings."""
        if not self.technologies:
            return []
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Database', 'Database & ORM'),
        ('Tools', 'Tools, Cloud & DevOps'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Backend')
    proficiency = models.IntegerField(default=85, help_text="Proficiency percentage (1 to 100)")
    icon = models.CharField(max_length=50, default="code", help_text="Lucide or FontAwesome icon slug (e.g. python, database, layout, terminal)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Experience(models.Model):
    TYPE_CHOICES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
    ]

    title = models.CharField(max_length=150, help_text="Role name or Degree name")
    organization = models.CharField(max_length=150, help_text="Company or University name")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='work')
    start_date = models.CharField(max_length=50, help_text="e.g., Jan 2023")
    end_date = models.CharField(max_length=50, default="Present", help_text="e.g., Dec 2024 or Present")
    description = models.TextField(help_text="Key responsibilities, courses, or achievements")
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} at {self.organization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email}) - {self.subject}"
