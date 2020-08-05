from django.urls import include, path
from . import views

urlpatterns = [

    path('users/', views.users, name='user'),
    path('', views.index, name='index'),
    path('articles/<int:article_id>', views.article, name='article'),
]
