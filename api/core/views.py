from rest_framework import viewsets
from rest_framework import permissions
from .models import (
    User,
    Company,
    GarbageType,
    GarbageSource,
    GarbageRequest,
    GarbageCollectionOrder,
    SubscriptionPlan,
    UserSubscription,
)
from .serializers import (
    UserSerializer,
    CompanySerializer,
    GarbageTypeSerializer,
    GarbageSourceSerializer,
    GarbageRequestSerializer,
    GarbageCollectionOrderSerializer,
    SubscriptionPlanSerializer,
    UserSubscriptionSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class GarbageTypeViewSet(viewsets.ModelViewSet):
    queryset = GarbageType.objects.all()
    serializer_class = GarbageTypeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class GarbageSourceViewSet(viewsets.ModelViewSet):
    queryset = GarbageSource.objects.all()
    serializer_class = GarbageSourceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class GarbageRequestViewSet(viewsets.ModelViewSet):
    queryset = GarbageRequest.objects.all()
    serializer_class = GarbageRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
 

class GarbageCollectionOrderViewSet(viewsets.ModelViewSet):
    queryset = GarbageCollectionOrder.objects.all()
    serializer_class = GarbageCollectionOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionPlanViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
