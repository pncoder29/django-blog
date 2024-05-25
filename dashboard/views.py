from django.shortcuts import render
from blogs_app.models import Blog, Category

#login required decorator
from django.contrib.auth.decorators import login_required

#
@login_required(login_url='login')
#This view is for dashboard
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        "category_count":category_count,
        "blogs_count":blogs_count,
    }
    return render(request, "dashboard/dashboard.html", context)
