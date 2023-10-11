from rest_framework import permissions


class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if request.user.is_staff:
            if user.has_perm('products.view_product'):
                return True
            return False
        return False

