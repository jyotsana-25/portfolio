from django.contrib import admin
from .models import Project, Skill, Experience, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at', 'github_url', 'live_demo_url')
    list_filter = ('category', 'featured', 'created_at')
    search_fields = ('title', 'summary', 'technologies', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order', 'icon')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('proficiency', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'type', 'start_date', 'end_date', 'is_current', 'order')
    list_filter = ('type', 'is_current')
    search_fields = ('title', 'organization', 'description')
    list_editable = ('order', 'is_current')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable = ('is_read',)
