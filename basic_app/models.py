
from django.db import models
from django.contrib.auth.models import BaseUserManager,PermissionsMixin,AbstractBaseUser
# Create your models here.
from django.utils import timezone


class TokenModel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    img=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Categories(models.Model):
    categoryname=models.CharField(max_length=200, blank=True)
    category_uz=models.CharField(max_length=200, blank=True)
    category_ru=models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.categoryname


class MyManager(BaseUserManager):
    def create_user(self, username, **extra):
        if not username:
            raise ValueError('Username kiritilishi majburiy !')
        
        user=self.model(username=username, **extra)
        user.set_password(extra.get('password'))
        user.save()
        return user
    
    def create_superuser(self, username, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_active', True)
        extra.setdefault('is_superuser', True)
        
        
        if not extra.get('is_staff'):
            raise ValueError("Superuser uchun is_staff True bo'lishi kerak")
        if not extra.get('is_active'):
            raise ValueError("Superuser uchun is_active True bo'lishi kerak")
        if not extra.get('is_superuser'):
            raise ValueError("Superuser uchun is_superuser True bo'lishi kerak")
        
        return self.create_user(username=username, **extra)
        
         
    
    
class MyUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=30, unique=True)
    phone=models.CharField(max_length=30, unique=True, default=None, null=True, blank=True)
    email=models.EmailField(unique=True)
    
    date_joined=models.DateTimeField(auto_now_add=True)
    
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    
    USERNAME_FIELD='username'
    REQUIRED_FIELD=[]
    
    objects=MyManager()
    
    def __str__(self):
        return self.username

class Site(models.Model):
    tel=models.CharField(max_length=30, verbose_name='Телефонный номер')
    address_ru=models.CharField(max_length=150, verbose_name='Адрес')
    address_uz=models.CharField(max_length=150, verbose_name='Адрес')
    time_ru=models.CharField(max_length=100, verbose_name='Рабочее времяxx', blank=True)
    time_uz=models.CharField(max_length=100, verbose_name='Рабочее времяxx', blank=True)
    telegram=models.CharField(max_length=100, verbose_name='Телеграм', blank=True)
    instagram=models.CharField(max_length=100, verbose_name='Инстаграм', blank=True)
    def __str__(self) -> str:
        return self.tel
    
    
class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True)
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    old_price=models.CharField(max_length=200, blank=True)
    dis_price=models.CharField(max_length=200, blank=True)
    quantity=models.CharField(max_length=100, blank=True)
    ramka_uz=models.CharField(max_length=200, blank=True)
    ramka_ru=models.CharField(max_length=200, blank=True)
    razmer_m=models.CharField(max_length=200, blank=True)
    razmer_sm=models.CharField(max_length=200, blank=True)
    recommendation_uz=models.CharField(max_length=200, blank=True)
    recommendation_ru=models.CharField(max_length=200, blank=True)
    complekt_uz=models.CharField(max_length=200, blank=True)
    complekt_ru=models.CharField(max_length=200, blank=True)
    

    def __str__(self):
        return self.category
    


class Zakaz(models.Model):
    image=models.ImageField(upload_to='images/', blank=True)
    name=models.CharField(max_length=60, verbose_name='Ваше имя')
    phone=models.CharField(max_length=40, verbose_name='Ваше номер')
    pool_frame=models.CharField(max_length=100, blank=True)
    money=models.CharField(max_length=100, blank=True)
    address=models.CharField(max_length=100, blank=True)
    date=models.DateTimeField(auto_now_add=True, blank=True)
    active=models.BooleanField()
    count=models.BigIntegerField(blank=True)
    product_name=models.CharField(max_length=100, blank=True)
    
    
    def __str__(self):
        return self.name
    
class Konsultatsiya(models.Model):  
    name=models.CharField(max_length=60, verbose_name='Ваше имя', blank=True)
    phone=models.CharField(max_length=40, verbose_name='Ваше номер', blank=True)
    date=models.DateTimeField(auto_now_add=True, blank=True)
    active=models.BooleanField()
    
    def __str__(self):
        return self.name

class Sinov(models.Model):
    name=models.ManyToManyField(Konsultatsiya)