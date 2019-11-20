from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from employee_meetings_api.models import EmployeeProfile
from employee_meetings_api.models import MeetingRoom
from employee_meetings_api.models import Room
from employee_meetings_api.models import Reservation
from employee_meetings_api.serializers import EmployeeProfileSerializer
from employee_meetings_api.serializers import MeetingRoomSerializer
from employee_meetings_api.serializers import RoomSerializer
from employee_meetings_api.serializers import ReservationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


from employee_meetings_api import permissions

class MeetingRoomList(generics.ListCreateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    name = 'meetingroom-list'


class MeetingRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    name = 'meetingroom-detail'


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-list'


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    name = 'room-detail'


class EmployeeProfileList(generics.ListCreateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    name = 'employee-profile-list'


class EmployeeProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    name = 'employee-profile-detail'
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(employee_profile=self.request.employee)


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-list'


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'meeting-rooms': reverse(MeetingRoomList.name,
            request=request),
            'rooms': reverse(RoomList.name, request=request),
            'employee_profiles': reverse(EmployeeProfileList.name, request=request),
            'reservations': reverse(ReservationList.name, request=request)
            })


class EmployeeLoginApiView(ObtainAuthToken):
    """Handle creating employee authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
