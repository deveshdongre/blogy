from django.urls import include, path
from . import views
from .views import SignUpView

urlpatterns = [

    path('', views.users, name='user'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
