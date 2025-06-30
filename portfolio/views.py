from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Project, CodeSample, BlogPost, Contact, Skill

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_projects'] = Project.objects.filter(featured=True)[:3]
        context['recent_posts'] = BlogPost.objects.filter(published=True)[:3]
        return context

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all().order_by('category', 'name')
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 6

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'


class CodeSampleListView(ListView):
    model = CodeSample
    template_name = 'portfolio/code_sample_list.html'
    context_object_name = 'code_sample_list'  # Changed to match template expectations
    paginate_by = 10


class CodeSampleDetailView(DetailView):
    model = CodeSample
    template_name = 'portfolio/code_sample_detail.html'
    context_object_name = 'sample'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add related samples based on same language or tags
        current_sample = self.get_object()
        related_samples = CodeSample.objects.filter(
            language=current_sample.language
        ).exclude(id=current_sample.id)[:3]

        context['related_samples'] = related_samples
        return context

class BlogListView(ListView):
    model = BlogPost
    template_name = 'portfolio/blog_list.html'
    context_object_name = 'blog_list'
    queryset = BlogPost.objects.filter(published=True)
    paginate_by = 5

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    queryset = BlogPost.objects.filter(published=True)
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ContactView(CreateView):
    model = Contact
    template_name = 'portfolio/contact.html'
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        messages.success(self.request, 'Thank you! Your message has been sent successfully.')
        return super().form_valid(form)