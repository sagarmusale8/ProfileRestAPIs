from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow Users to edit thier own profiles"""

    def has_object_permission(self, request, view, obj):
        """ Checks if user has permission"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id