from django.urls import path
from . import views

urlpatterns = [
    #this path for dashbaord with emptry string
    path('', views.dashboard, name="dashboard"),
    
    #sidebar and liniking
    path("categories/", views.categories, name="categories"),
]