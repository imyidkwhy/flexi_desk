from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    username = models.CharField(max_length=45, unique=True)
    phone_number = models.CharField(max_length=18, blank=True, null=True)
    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class Spot(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "AV", "Available"
        BUSY = "BU", "Busy"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='spots/', null=True, blank=True)
    floor = models.IntegerField()
    cabinet = models.IntegerField()
    description = models.TextField(
        default="A modern workspace with high-speed internet.")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    size = models.IntegerField(default=20, help_text="Size in sq. meters")

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.AVAILABLE)

    def __str__(self):
        return self.title


class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} -> {self.spot}"
