from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Create a new user and return a User with an email, phone number, username and password."""
        if username is None:
            raise TypeError("User must have a username.")
        if email is None:
            raise TypeError("User must have an email.")

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Ceate and return a `User` with superuser (admin) permission."""

        if password is None:
            raise TypeError("Superuser must have a password.")
        if email is None:
            raise TypeError("Superuser must have an email.")
        if username is None:
            raise TypeError("Superuser must have a username.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todo_user = models.ForeignKey(User, on_delete=models.CASCADE)
