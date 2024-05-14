"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#this came from folder blogs_app pointing views.py 
from blogs_app import views as blogsview

urlpatterns = [
    #this path for admin
    path('admin/', admin.site.urls),
    
    #this path for home or index.html
    path("", views.home, name="home"),
    
    #this path for blogs_apps or your startapp project_name
    path("category/", include("blogs_app.urls")),
    
    #this path for slug urls
    path("blogs_app<slug:slug>/", blogsview.blogs, name="blogs"),
    
    #search endpoint
    path("blogs_app/search", blogsview.search, name="search"),
    
    #this path for registration
    path("register/", views.register, name="register"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
