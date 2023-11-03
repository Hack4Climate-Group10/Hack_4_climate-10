from django.urls import path, include
from django.contrib import admin
from core import views
urlpatterns = [
    
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/<int:user_id>/', views.user_detail_view, name='user-detail'),
    path('users/', views.list_users, name='user-list'),
    path('garbage-categories/', views.garbage_category_list, name='garbage-category-list'), 
    path('garbage-categories/<int:category_id>/', views.garbage_category_detail, name='garbage-category-detail'), 
    path('companies/', views.company_list, name='company-list'), 
    path('companies/<int:company_id>/', views.company_detail, name='company-detail'), 
    path('garbage-sources/', views.garbage_source_list, name='garbage-source-list'), 
    path('garbage-sources/<int:source_id>/', views.garbage_source_detail, name='garbage-source-detail'), 
    path('garbage-collection-orders/', views.garbage_collection_order_list, name='garbage-collection-order-list'), 
    path('garbage-collection-orders/<int:order_id>/', views.garbage_collection_order_detail, name='garbage-collection-order-detail'),
    path('subscription-plans/', views.subscription_plan_list, name='subscription-plan-list'), 
    path('subscription-plans/<int:plan_id>/', views.subscription_plan_detail, name='subscription-plan-detail'),


    
    
    
]

 