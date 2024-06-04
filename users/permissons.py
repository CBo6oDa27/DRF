from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором.
    Модератор не может создавать и удалять уроки и курсы."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(permissions.BasePermission):
    """Проверка на доступ к объекту только для владельца."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
