from django.urls import path
from . import views

urlpatterns = [
    #this part getting the foriegn key in category for views of post_by_category
    path("<int:category_id>/", views.post_by_category, name="post_by_category")
]