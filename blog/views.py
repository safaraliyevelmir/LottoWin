from django.shortcuts import get_object_or_404, render
from .models import Blog, BlogTitle
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

class BlogListView(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_title"] =BlogTitle.objects.first()
        return context
    

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_inner.html'
    context_object_name = 'blog'

    
    def get(self, request, slug):
        blog = get_object_or_404(Blog.objects.filter(slug=slug))
        blog.view += 1
        blog.save()
        last_posts = Blog.objects.all().order_by('-date')[:5]
        context = {
            'last_posts':last_posts,
            'blog':blog,
            'blog_title':blog_title,
        }
        return render(request, 'blog_inner.html',context)
        