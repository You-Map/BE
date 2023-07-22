from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class MyaccountManager(BaseUserManager):
    def create_user(self, email, username, name, univ, location, password=None, **extra_fields):
        
        if not email:
            raise ValueError('Email must be set')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
            univ = univ,
            location = location,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email,  password=None, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)

        

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=False)
    username = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    univ = models.CharField(max_length=255 ,null=False, blank=False)
    location = models.CharField(max_length=255)

    objects = MyaccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
