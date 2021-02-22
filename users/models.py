from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import LibrarianManager, CustomerManager, AdminManager


class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        LIBRARIAN = "LIBRARIAN", "Librarian"
        CUSTOMER = "CUSTOMER", "Customer"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    base_role = Roles.CUSTOMER

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=Roles.choices, blank=True, null=True, default=base_role, max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = self.base_role
        return super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    objects = AdminManager()

    def __str__(self):
        return self.email


class Admin(User):
    base_role = User.Roles.ADMIN
    objects = AdminManager()

    class Meta:
        proxy = True


class Librarian(User):
    base_role = User.Roles.LIBRARIAN
    objects = LibrarianManager()

    class Meta:
        proxy = True


class Customer(User):
    base_role = User.Roles.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True
