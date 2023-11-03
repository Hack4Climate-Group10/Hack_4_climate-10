from rest_framework import serializers
from .models import User, Company, GarbageType, GarbageSource, GarbageRequest, GarbageCollectionOrder, SubscriptionPlan, UserSubscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'created_at', 'address', 'phone')

class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Company
        fields = ('id', 'user', 'name', 'address', 'contact_name', 'contact_email', 'contact_phone', 'website', 'description')

class GarbageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GarbageType
        fields = ('id', 'name', 'description')

class GarbageSourceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = GarbageSource
        fields = ('id', 'user', 'name', 'source_type', 'address', 'contact_email', 'contact_phone', 'description')

class GarbageRequestSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    garbage_types = GarbageTypeSerializer(many=True)
    
    class Meta:
        model = GarbageRequest
        fields = ('id', 'user', 'collection_date_time', 'collection_status', 'notes', 'garbage_types')

class GarbageCollectionOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    source = GarbageSourceSerializer()
    garbage_types = GarbageTypeSerializer(many=True)
    
    class Meta:
        model = GarbageCollectionOrder
        fields = ('id', 'user', 'company', 'source', 'collection_date_time', 'collection_status', 'notes', 'garbage_types')

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ('id', 'name', 'description', 'price', 'features', 'billing_cycle')

class UserSubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()
    subscription_plan = SubscriptionPlanSerializer()
    
    class Meta:
        model = UserSubscription
        fields = ('id', 'user', 'company', 'subscription_plan', 'start_date', 'end_date', 'active')
