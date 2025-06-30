from django.contrib import admin
from .models import Skill, Project, CodeSample, BlogPost, Contact

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category']
    list_filter = ['level', 'category']
    search_fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'created_date', 'technologies']
    search_fields = ['title', 'description']
    filter_horizontal = ['technologies']
    prepopulated_fields = {'short_description': ('title',)}


@admin.register(CodeSample)
class CodeSampleAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'created_at', 'difficulty']  # Changed from created_date
    list_filter = ['language', 'created_at', 'difficulty']  # Changed from created_date
    search_fields = ['title', 'description', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'lines_of_code']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'language', 'difficulty')
        }),
        ('Code', {
            'fields': ('code', 'filename', 'lines_of_code')
        }),
        ('Additional Information', {
            'fields': ('complexity', 'usage_instructions', 'explanation', 'example_usage', 'github_url', 'tags'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_date']
    list_filter = ['published', 'created_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'read']
    list_filter = ['read', 'created_date']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_date']