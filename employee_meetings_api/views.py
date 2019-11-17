from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from employee_meetings_api import serializers
from  employee_meetings_api import models

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating employee profiles """
    serializer_class = serializers.EmployeeProfileSerializer
    queryset = models.EmployeeProfile.objects.all()
