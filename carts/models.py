from django.contrib.auth.models import User
from django.db import models
from medicines.models import Medicine


class Cart(models.Model):

    user = models.TextField(User)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


class MedicineOnCart(models.Model):

    med = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
