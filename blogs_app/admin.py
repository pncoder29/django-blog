from django.contrib import admin
from .models import Category, Blog

#this purpose for prepopulated fields for title slug
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    
    #list display 
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    
    #search field. and make it sure your category is pointed to your 1st model 'category__category_name'
    search_fields =('id', 'title', 'category__category_name', 'status')
    
    #this featured for edit specific model
    list_editable =("is_featured",)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)