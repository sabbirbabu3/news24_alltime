from django.shortcuts import render
from post.models import Article,Categories


def home(request, category_slug=None):
    data = Article.objects.all()
    if category_slug is not None:
        category = Categories.objects.get(slug=category_slug)
        data = Article.objects.filter(category =category)
    categories = Categories.objects.all()
    latest_posts = data.order_by('-publishing_time')[:3]
    return render(request, 'index.html', {'data': data, 'category': categories, 'latest_posts': latest_posts})


def home_Category(request, category_slug=None):
    data = Article.objects.all()
    if category_slug is not None:
        category = Categories.objects.get(slug=category_slug)
        data = Article.objects.filter(category =category)
    categories = Categories.objects.all()
    latest_posts = data.order_by('-publishing_time')[:3]
    return render(request, 'category.html', {'data': data, 'category': categories, 'latest_posts': latest_posts})

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')