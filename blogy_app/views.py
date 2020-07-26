from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def users(request):
    print(request)
    users = User.objects.all()
    print(users)
    return render(request, 'blogy_app/users.html', {'users': users})
