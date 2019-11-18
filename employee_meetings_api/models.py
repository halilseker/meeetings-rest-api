from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class EmployeeProfileManager(BaseUserManager):
    """Manager for employee profiles """

    def create_user(self, email, name, password=None):
        """Create a new employee profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        employee = self.model(email=email, name=name)

        employee.set_password(password)
        employee.save(using=self._db)

        return employee

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details """
        employee = self.create_user(email, name, password)

        employee.is_superuser = True
        employee.is_staff = True
        employee.save(using=self._db)

        return employee

class EmployeeProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for employees in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = EmployeeProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class EmployeeReservation(models.Model):
    """Employee status update """
    employee_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
