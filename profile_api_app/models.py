from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """creating Manager for UserProfile"""
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("please fill the email field")

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,email,password):
        """create and save new superuser"""
        user = self.create_user(name,email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """data base model for user"""

    email = models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """gettting the full name"""
        return self.name

    def get_short_name(self):
        """getting short name"""
        return self.name