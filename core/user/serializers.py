from core.user.models import User, Todo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "created_at", "updated_at"]
        read_only_fields = ["is_active", "created_at", "updated_at"]


class TodoSerializer(serializers.ModelSerializer):
    models = Todo
    fields = ["id", "title", "description", "completed", "created_at", "updated_at"]
