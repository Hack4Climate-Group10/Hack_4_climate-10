from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from core.views import (
    UserViewSet,
    CompanyViewSet,
    GarbageTypeViewSet,
    GarbageSourceViewSet,
    GarbageRequestViewSet,
    GarbageCollectionOrderViewSet,
    SubscriptionPlanViewSet,
    UserSubscriptionViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'garbage-types', GarbageTypeViewSet)
router.register(r'garbage-sources', GarbageSourceViewSet)
router.register(r'garbage-requests', GarbageRequestViewSet)
router.register(r'garbage-collection-orders', GarbageCollectionOrderViewSet)
router.register(r'subscription-plans', SubscriptionPlanViewSet)
router.register(r'user-subscriptions', UserSubscriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('admin/', admin.site.urls),  
]
