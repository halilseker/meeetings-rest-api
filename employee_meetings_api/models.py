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


class MeetingRoom(models.Model):
    """Meeting room used for reservations"""
    meeting_type = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return self.meeting_type


class Room(models.Model):
    """ Room used for meetings"""
    room_name = models.CharField(max_length=255)
    meeting_room = models.ForeignKey(
        MeetingRoom,
        related_name= 'rooms',
        on_delete=models.CASCADE
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        """Return the model as a string"""
        return self.room_name

class Reservation(models.Model):
    """Employees attends for meeting"""
    employee_profile = models.ForeignKey(
        EmployeeProfile,
        related_name= 'reservations',
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    limit = models.IntegerField()

    def __str__(self):
        """Return the model as a string"""
        return self.limit
