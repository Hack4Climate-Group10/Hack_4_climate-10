from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
'''
waste categories 
'''
class Company(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField()  
    def __str__(self):
        return self.name 
    
'''
waste categories 
'''
class GarbageType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name 
  
  
class GarbageSource(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    source_type = models.CharField(max_length=255) 
    address = models.TextField() 
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15) 
    description = models.TextField() 

    def __str__(self):
        return self.name
  

class GarbageRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    collection_date_time = models.DateTimeField()
    collection_status = models.CharField(max_length=20)  
    notes = models.TextField()
    garbage_types = models.ManyToManyField(GarbageType) 

    def __str__(self):
        return f"Request ID: {self.id}, User: {self.user.username}, Status: {self.collection_status}, Date: {self.collection_date_time}"


class GarbageCollectionOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  
    source = models.ForeignKey(GarbageSource, on_delete=models.CASCADE)   
    collection_date_time = models.DateTimeField()
    collection_status = models.CharField(max_length=20)  
    notes = models.TextField()
    garbage_types = models.ManyToManyField(GarbageType)    

    def __str__(self):
        return f"Order ID: {self.id}, User: {self.user.username}, Status: {self.collection_status}, Date: {self.collection_date_time}"



class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    billing_cycle = models.CharField(max_length=20) 
    
    def __str__(self):
        return self.name
    
    
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)  
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Subscription for {self.user.username} with {self.company.name}"
