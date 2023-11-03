from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import  *
from .models import *

@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({'message': 'Registration successful', 'tokens': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response({'message': 'Login successful', 'tokens': token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail_view(request, user_id):
    try: 
        user = request.user if user_id == 'self' else User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user == user or request.user.is_staff:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User information updated successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        if request.user == user or request.user.is_staff:
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAdminUser])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def garbage_category_list(request):
    if request.method == 'GET':
        categories = GarbageType.objects.all()
        serializer = GarbageTypeSerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GarbageTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage category created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def garbage_category_detail(request, category_id):
    try:
        category = GarbageType.objects.get(pk=category_id)
    except GarbageType.DoesNotExist:
        return Response({'error': 'Garbage category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GarbageTypeSerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GarbageTypeSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage category updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': 'Garbage category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




# company view

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = CompanySerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Company created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = CompanySerializer(company, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Company updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response({'message': 'Company deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
# sources view

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def garbage_source_list(request):
    if request.method == 'GET':
        sources = GarbageSource.objects.all()
        serializer = GarbageSourceSerializer(sources, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = GarbageSourceSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage source created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def garbage_source_detail(request, source_id):
    try:
        source = GarbageSource.objects.get(pk=source_id)
    except GarbageSource.DoesNotExist:
        return Response({'error': 'Garbage source not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GarbageSourceSerializer(source)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = GarbageSourceSerializer(source, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage source updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        source.delete()
        return Response({'message': 'Garbage source deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    

# view for gabbage rewuest
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def garbage_request_list(request):
    if request.method == 'GET':
        requests = GarbageRequest.objects.filter(user=request.user)  
        serializer = GarbageRequestSerializer(requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = GarbageRequestSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage request created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def garbage_request_detail(request, request_id):
    try:
        request_instance = GarbageRequest.objects.get(pk=request_id)
    except GarbageRequest.DoesNotExist:
        return Response({'error': 'Garbage request not found'}, status=status.HTTP_404_NOT_FOUND)

    if request_instance.user != request.user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = GarbageRequestSerializer(request_instance)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = GarbageRequestSerializer(request_instance, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage request updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        request_instance.delete()
        return Response({'message': 'Garbage request deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def garbage_collection_order_list(request):
    if request.method == 'GET':
        orders = GarbageCollectionOrder.objects.filter(user=request.user)  
        serializer = GarbageCollectionOrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = GarbageCollectionOrderSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage collection order created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def garbage_collection_order_detail(request, order_id):
    try:
        order = GarbageCollectionOrder.objects.get(pk=order_id)
    except GarbageCollectionOrder.DoesNotExist:
        return Response({'error': 'Garbage collection order not found'}, status=status.HTTP_404_NOT_FOUND)

    if order.user != request.user:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        serializer = GarbageCollectionOrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT': 
        serializer = GarbageCollectionOrderSerializer(order, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Garbage collection order updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Garbage collection order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# subscription plan


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def subscription_plan_list(request):
    if request.method == 'GET':
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Subscription plan created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def subscription_plan_detail(request, plan_id):
    try:
        plan = SubscriptionPlan.objects.get(pk=plan_id)
    except SubscriptionPlan.DoesNotExist:
        return Response({'error': 'Subscription plan not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionPlanSerializer(plan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubscriptionPlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Subscription plan updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plan.delete()
        return Response({'message': 'Subscription plan deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
    

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def user_subscription_list(request):
    if request.method == 'GET':
        subscriptions = UserSubscription.objects.all()
        serializer = UserSubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User subscription created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def user_subscription_detail(request, subscription_id):
    try:
        subscription = UserSubscription.objects.get(pk=subscription_id)
    except UserSubscription.DoesNotExist:
        return Response({'error': 'User subscription not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSubscriptionSerializer(subscription)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User subscription updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subscription.delete()
        return Response({'message': 'User subscription deleted successfully'}, status=status.HTTP_204_NO_CONTENT)