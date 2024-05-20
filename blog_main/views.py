from django.shortcuts import redirect, render
from blogs_app.models import Blog, Category
from blogs_app.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    # Fetching categories from your database
    # categories = Category.objects.all()
    
    # Fetching featured blog posts using object filter with status
    featured_posts = Blog.objects.filter(is_featured=True, status="published")
    posts = Blog.objects.filter(is_featured=False, status="published")
    
    # Sending your data into your HTML or frontend
    context = { 
        # "categories": categories,
        "featured_posts": featured_posts,
        "posts": posts,
    }
    return render(request, 'index.html', context)

#this views for registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #validation if request data is correct
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors) 
    else:
        form = RegistrationForm()
    context ={
        "form": form,
    }
    return render(request, "register.html", context)


#this view is for login
def login(request):
    form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "login.html", context)