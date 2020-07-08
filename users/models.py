from django.contrib.auth.models import AbstractUser
from django.db import models

from carts.models import Cart

user_type = (
        ('pharmacist', 'Pharmacist'),
        ('manager', 'Medical Repository Manager'),
    )


class CustomUser(AbstractUser):

    user_type = models.CharField(max_length=50, choices=user_type)

    def __str__(self):
        return self.username

   # def save(self, *args, **kwargs):
    #    super(CustomUser, self).save(*args, **kwargs)
     #   Cart.objects.create(user=self)
      #  return

