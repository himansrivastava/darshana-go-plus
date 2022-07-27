from django.db import models


class Institute(models.Model):
    """Model class for institue"""

    class Status(models.TextChoices):
        """Status enum for institue"""

        ACTIVE = ("Active",)
        INACTIVE = ("InActive",)
        ABOUTTOEXPIRE = ("AboutToExpire",)
        CANCELLED = ("Cancelled",)

    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=Status.choices)
