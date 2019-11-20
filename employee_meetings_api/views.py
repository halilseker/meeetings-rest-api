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
