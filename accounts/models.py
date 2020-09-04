from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name = None, last_name = None, password = None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.staff  = is_staff
        user_obj.admin  = is_admin
        user_obj.active = is_active
        user_obj.save(using = self._db)
        return user_obj

    def create_staffuser(self, email, first_name = None, last_name = None, password = None):
        user = self.create_user (
            email, 
            first_name = first_name,
            last_name = last_name,
            password = password,
            is_staff = True
        )
        return user
    
    def create_superuser(self, email, first_name = None, last_name = None, password = None):
        user = self.create_user (
            email, 
            first_name = first_name,
            last_name = last_name,
            password = password,
            is_staff = True,
            is_admin = True
        )
        return user


class User(AbstractBaseUser):
    email      = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name  = models.CharField(max_length=255, blank=True, null=True)
    active     = models.BooleanField(default=True)
    staff      = models.BooleanField(default=False)
    admin      = models.BooleanField(default=False)
    timestamp  = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['last_name']

    objects   = UserManager()

    def __str__(self):
        return self.email

    def get_first_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def get_last_name(self):
        if self.last_name:
            return self.last_name
        return self.email

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    def has_perm(self, perm, obj=None):
       return self.is_admin

    def has_module_perms(self, app_label):
       return self.is_admin

 
    @property 
    def is_active(self):
        return self.active

class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.user.first_name





