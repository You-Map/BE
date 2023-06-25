from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class MyaccountManager(BaseUserManager):
    def create_user(self, email, username, name, univ, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('Use must have an userID')
        if not name:
            raise ValueError('User must have a name')
        if not univ:
            raise ValueError('User must have a univ name')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            name = name,
            univ = univ
        )

        user.set_password(password)
        user.save(suing=self.db)
        return user
    
    def create_superuser(self, email, username, name,univ, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            name=name,
            password=password,
            univ=univ
        )
        user.is_superuser = True
        user.save(using=self.db)
        return user

        

class Account(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True,blank=False)
    username = models.CharField(max_length=20, unique=True,blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    is_superuser = models.BooleanField(default = False)
    univ = models.CharField(max_length=30,null=False,blank=False )
    objects = MyaccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'univ']

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, onj=None):
        return self.is_superuser