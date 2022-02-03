from django.contrib.auth.models import AbstractUser,UserManager


class User(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username
