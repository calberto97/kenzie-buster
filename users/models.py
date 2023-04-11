from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)


# class CustomUserManager(BaseUserManager):
#     def create_superuser(self, email, first_name, last_name, password=None):
#         user = self.create_user(email, first_name, last_name, password)
#         user.is_employee = True
#         user.is_superuser = True

#         user.save()
#         return user


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=127, unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)

    # def create(self, email, first_name, last_name, password=None):
    #     self.is_employee = False
    #     self.is_superuser = False
    def __repr__(self) -> str:
        return f"<User ({self.id} - {self.name})>"

    pass
