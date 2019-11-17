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
