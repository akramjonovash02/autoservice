from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Employee':
            return True
        else:
            return False

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'Customer':
            return True
        else:
            return False