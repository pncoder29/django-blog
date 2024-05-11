from blogs_app.models import Category

#context processors is passing data from base.html using dict
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)