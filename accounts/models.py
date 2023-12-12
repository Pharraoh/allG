from django.db import models

# models.py (in your custom user model)
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class MyUserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, email, password, **extra_fields)
#
# class MyUser(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     # Add any additional fields you need
#
#     objects = MyUserManager()
#
#     USERNAME_FIELD = 'username'
#     EMAIL_FIELD = 'email'
