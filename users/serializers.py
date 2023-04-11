from django.db.models.fields import SlugField
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")]
    )
    email = serializers.EmailField(
        max_length=127,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")]
    )
    password = serializers.CharField(max_length=127, write_only=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data) -> User:
        if validated_data["is_employee"]:
            validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)
