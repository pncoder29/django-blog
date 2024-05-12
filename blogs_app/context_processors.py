from blogs_app.models import Category, social_link

#context processors is passing data from base.html using dict
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

# Assuming your model is named SocialLink
def get_social_link(request):
    social_links = social_link.objects.all()
    return dict(social_links = social_links)
