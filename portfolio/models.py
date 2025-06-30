from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ])
    category = models.CharField(max_length=50, choices=[
        ('programming', 'Programming Languages'),
        ('framework', 'Frameworks'),
        ('database', 'Databases'),
        ('tool', 'Tools & Technologies'),
        ('other', 'Other'),
    ])
    
    def __str__(self):
        return f"{self.name} ({self.level})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for project cards")
    technologies = models.ManyToManyField(Skill, related_name='projects')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})

class CodeSample(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html-css', 'HTML/CSS'),
        ('django', 'Django'),
        ('sql', 'SQL'),
        ('bash', 'Bash'),
        ('json', 'JSON'),
        ('algorithms', 'Algorithms'),
        ('other', 'Other'),
    ]

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    code = models.TextField()
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, blank=True, null=True)
    tags = models.CharField(max_length=200, help_text="Comma-separated tags", blank=True)

    # Additional fields referenced in templates
    filename = models.CharField(max_length=100, blank=True, help_text="Optional filename for the code")
    lines_of_code = models.IntegerField(blank=True, null=True)
    complexity = models.CharField(max_length=50, blank=True, help_text="Big O notation, e.g., 'n log n'")
    usage_instructions = models.TextField(blank=True, help_text="How to use this code")
    explanation = models.TextField(blank=True, help_text="Detailed explanation of the code")
    example_usage = models.TextField(blank=True, help_text="Example of how to use the code")
    github_url = models.URLField(blank=True, help_text="Link to GitHub repository")

    created_date = models.DateTimeField(auto_now_add=True)  # Keep this temporarily
    created_at = models.DateTimeField(default=timezone.now)  # Add with default
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Copy created_date to created_at if needed
        if self.created_date and not self.created_at:
            self.created_at = self.created_date

        # Auto-calculate lines of code if not provided
        if not self.lines_of_code and self.code:
            self.lines_of_code = len([line for line in self.code.split('\n') if line.strip()])

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('code_sample_detail', kwargs={'slug': self.slug})

    def get_tags_list(self):
        """Return list of tags for template compatibility"""
        if self.tags:
            return [{'name': tag.strip()} for tag in self.tags.split(',') if tag.strip()]
        return []

    # Template compatibility properties
    @property
    def tags_objects(self):
        """Mock tags.all() for template compatibility"""

        class MockTagManager:
            def all(self):
                return [{'name': tag.strip()} for tag in self.tags.split(',') if tag.strip()]

        return MockTagManager()

    # Mock related fields for template compatibility
    @property
    def dependencies(self):
        class MockDependencyManager:
            def all(self):
                return []  # Return empty list or implement actual dependencies

        return MockDependencyManager()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, help_text="Brief summary for blog list")
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def reading_time(self):
        word_count = len(self.content.split())
        return max(1, word_count // 200)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"