from rest_framework import serializers

from employee_meetings_api import models


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

class ReservationSerializer(serializers.ModelSerializer):
    """Serializes reservation """

    class Meta:
        model = models.Reservation
        fields = ('id', 'employee_profile', 'status_text', 'created_on', 'title')
        extra_kwargs = {'employee_profile': {'read_only': True}}


class MeetingRoomSerializer(serializers.ModelSerializer):
    """Serializes MeetingRoom """

    class Meta:
        model = models.MeetingRoom
        fields = ('id', 'employee_profile', 'is_available')
        extra_kwargs = {'employee_profile': {'read_only': True}}
