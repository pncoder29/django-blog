from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category
from django.db.models import Q

# fetch requesting for category ID with catheory_id
def post_by_category(request, category_id):
    # fetch post belong to category with category_id
    posts = Blog.objects.filter(status="published", category=category_id)
    
    # we use get ofr category in order to fetch data 1 by 1
    # we use try/except when some custom category does not exist
    try:
        category = Category.objects.get(pk = category_id)
    except:
        #redirecting user to homepage
        return redirect("home")
    # Use get_object_or_404 if you want to show 404 page
    # category = get_object_or_404(Category, pk=category_id)
    
    context ={
        "posts": posts,
        "category": category,
    }
    return render(request, "post_by_category.html", context)


#this function for blogs with slug
def blogs(request, slug):
    
    #blog post for slug and status published 
    single_blog = get_object_or_404(Blog, slug=slug, status="published")
    context ={
        "single_blog": single_blog,
    }
    return render(request, "blogs.html", context)

#this is search area keyword title, short description, blog body with Q objects
def search(request):
    
    #search term
    keyword = request.GET.get("keyword")
    
    #keyword title, short description, blog body with Q objects
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="published")
    context ={
        "blogs": blogs,
        "keyword": keyword,
    }
    return render(request, "search.html", context)