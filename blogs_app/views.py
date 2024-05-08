from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

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