from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow employee to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """Check employee is tyrying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        # return obj.id == request.employee.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
