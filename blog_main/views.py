from django.shortcuts import render
from blogs_app.models import Category

def home(request):
    
    #Featchng category in your database
    categories = Category.objects.all()
    
    #sending your data into your HTML or frontend
    context = { 
        "categorie": categories,
    }
    return render(request, 'index.html', {'categories': categories})