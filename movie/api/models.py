from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
 
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)
 
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
 
    def created(self):
        self.created_date = timezone.now()
        self.save()
 
    def updated(self):
        self.updated_date = timezone.now()
        self.save()

class CustomUser(AbstractUser):
    email = models.CharField(blank=False, max_length=30)
    customusername = models.CharField(blank=False, max_length=20)
    password = models.CharField(blank=False, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.username
    def _create_customuser(self, username, email, password,
                    phone, address, city, country):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        customuser = self.model(username=username, email=email, phone=phone, address=address,city=city, country=country)
        customuser.set_password(password)
        customuser.save(using=self._db)
        return customuser
    def create_customuser(self, username, email, password,
                    phone, address, city, country):
        return self._create_user(self, username, email, password,
                    phone, address, city, country)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)