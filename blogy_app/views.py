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
