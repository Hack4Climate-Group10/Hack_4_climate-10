from django.urls import path, include
from django.contrib import admin
from core import views
urlpatterns = [
    
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/<int:user_id>/', views.user_detail_view, name='user-detail'),
    path('users/', views.list_users, name='user-list'),
    
]

 