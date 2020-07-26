from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.users, name='user'),
]
