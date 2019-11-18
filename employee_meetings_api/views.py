from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from employee_meetings_api import serializers
from  employee_meetings_api import models
from employee_meetings_api import permissions


class EmployeeProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating employee profiles """
    serializer_class = serializers.EmployeeProfileSerializer
    queryset = models.EmployeeProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
