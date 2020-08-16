from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Articles, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def users(request):
    print(request)
    users = User.objects.all()
    print(users)
    return render(request, 'blogy_app/users.html', {'users': users})


@login_required()
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
        next_url = request.GET.get('next')
        if user is not None:
            login(request, user)
            if next_url is not None:
                return redirect(next_url)
            # Redirect to a success page.
            return redirect(index)
        else:
            return render(request, 'blogy_app/login.html', {})
    else:
        if request.user.is_authenticated:
            return redirect(index)
        return render(request, 'blogy_app/login.html', {})


def logout_route(request):
    logout(request)
    return redirect('login_route')


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
