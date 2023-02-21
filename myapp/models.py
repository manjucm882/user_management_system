from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('The email field must be set')
        user = self.model(email=self.normalize_emial(email),**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password = None,**kwargs):
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_superuser',True)
        return self.create_user(email,password,**kwargs)
    
class User(AbstractBaseUser):
    email = models.EmailField(unique=True,max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email