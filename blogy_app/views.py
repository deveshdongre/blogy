from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Articles
# Create your views here.


def users(request):
    print(request)
    users = User.objects.all()
    print(users)
    return render(request, 'blogy_app/users.html', {'users': users})


def index(request):
    articles = Articles.objects.all()
    return render(request, 'blogy_app/index.html', {'articles': articles})


def article(request, article_id):
    article = Articles.objects.filter(id=article_id)

    return render(request, 'blogy_app/article.html', {'art': article and len(article) > 0 and article[0]})
