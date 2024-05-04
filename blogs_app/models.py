from django.db import models
from django.contrib.auth.models import User

# Create your models here. every changing models must be make and migrates
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Correting spelling with using verbose method
    class Meta:
        verbose_name_plural = 'categories'
    
    #A object type that convert to string display 
    def __str__(self):
        return self.category_name

#Status for knowing publishing content status choices
STATUS_CHOICES =(
    ("draft", "Draft"),
    ("published", "Published"),
)

#Create model for blogs. every changing models must be make and migrates
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_img = models.ImageField(upload_to="uploads/%y/%m/%d")
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #A object type that convert to string display 
    def __str__(self):
        return self.title