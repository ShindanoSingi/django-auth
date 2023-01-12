from core.user.serializers import UserSerializer, TodoSerializer

from core.user.models import User, Todo
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

class UserViewSet(models.ModelViewSet):
    http_method_names = ['get']
    serializers_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated_at', 'created_at']
    ordering = ['-updated']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj

class TodoViewSet(viewsets.ModelViewSet):
    serializers_class = TodoSerializer

    def get_queryset(self):

        return Todo.objects.all()