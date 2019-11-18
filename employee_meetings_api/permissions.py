from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow employee to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """Check employee is tyrying to edit theri own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
