from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def social(request):
    return render(request, 'blog/social.html')

def blog_page(request, slug):
    post = Post.objects.get(slug=slug)
    template_name = f"blog/uploads/{slug}.html"
    return render(request, template_name, {'post': post})
