from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    PermissionsMixin,
)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=127, unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)

    def __repr__(self) -> str:
        return f"<User ({self.id} - {self.email})>"
