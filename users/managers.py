from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class AdminManager(UserManager):

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', "ADMIN")

        if extra_fields.get('role') != 'ADMIN':
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='ADMIN')


class LibrarianManager(UserManager):

    def create_librarian(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('role', "LIBRARIAN")
        return self.create_user(email, password, **extra_fields)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='LIBRARIAN')


class CustomerManager(UserManager):

    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('role', "CUSTOMER")
        return self.create_user(email, password, **extra_fields)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role='CUSTOMER')
