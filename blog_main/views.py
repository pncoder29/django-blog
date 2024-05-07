from django.shortcuts import render
from blogs_app.models import Blog, Category

def home(request):
    # Fetching categories from your database
    categories = Category.objects.all()
    
    # Fetching featured blog posts using object filter with status
    featured_posts = Blog.objects.filter(is_featured=True, status="published")
    posts = Blog.objects.filter(is_featured=False, status="published")
    
    # Sending your data into your HTML or frontend
    context = { 
        "categories": categories,
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, 'index.html', context)
