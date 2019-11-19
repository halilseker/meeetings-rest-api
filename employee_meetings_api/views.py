from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

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


class EmployeeLoginApiView(ObtainAuthToken):
    """Handle creating employee authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ReservationViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating reservation"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ReservationSerializer
    queryset = models.Reservation.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
        # IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the employee profile to the logged in user """
        serializer.save(employee_profile=self.request.employee)


class MeetingRoomViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating meeting room"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.MeetingRoomSerializer
    queryset = models.MeetingRoom.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
        # IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the employee profile to the logged in user """
        serializer.save(employee_profile=self.request.employee)
