from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Articles, Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
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


def update(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Hi this is updated BIO'
    user.save()


def login_route(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(index)
        else:
            pass
    else:
        return render(request, 'blogy_app/login.html', {})


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            user.refresh_from_db()
            user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(index)
    else:
        form = UserCreateForm()
    return render(request, 'blogy_app/register.html', {'form': form})
