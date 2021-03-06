from rest_framework import serializers
from employee_meetings_api.models import EmployeeProfile
from employee_meetings_api.models import MeetingRoom
from employee_meetings_api.models import Room
from employee_meetings_api.models import Reservation
from employee_meetings_api import models
import employee_meetings_api.views


class EmployeeProfileSerializer(serializers.ModelSerializer):
    """Serializes a employee profile object"""
    class Meta:
        model = models.EmployeeProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new employee profile"""
        employee = models.EmployeeProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return employee


class MeetingRoomSerializer(serializers.HyperlinkedModelSerializer):

    rooms = serializers.HyperlinkedRelatedField(
	      many=True,
	      read_only=True,
	      view_name='room-detail')

    class Meta:
        model = models.MeetingRoom
        fields = ('id', 'meeting_type', 'rooms')


class RoomSerializer(serializers.ModelSerializer):
    """Serializes a room object"""
    meeting_room = serializers.PrimaryKeyRelatedField(
        # read_only = True,
        queryset=MeetingRoom.objects.all()
    )

    class Meta:
        model = models.Room
        fields = ('id', 'room_name', 'is_available', 'meeting_room')


class ReservationSerializer(serializers.ModelSerializer):
    """Serialize a reservation"""
    room = serializers.PrimaryKeyRelatedField(
        # many=True,
        queryset=Room.objects.all()
    )
    employee_profile = serializers.PrimaryKeyRelatedField(
        # many=True,
        queryset=EmployeeProfile.objects.all(),
    )

    class Meta:
        model = Reservation
        fields = ('id', 'title', 'created_on', 'limit', 'employee_profile', 'room')
        read_only_fields = ('id','employee_profile','room_name')
