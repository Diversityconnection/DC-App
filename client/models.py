from enum import Enum
from django.db import models
from cuser.models import CUser


class ClientRole(str, Enum):
    CUSTOMER = "customer"
    SELLER = "seller"

    @classmethod
    def all(cls):
        return [
            ClientRole.CUSTOMER,
            ClientRole.SELLER,
        ]


class Client(models.Model):
    user = models.OneToOneField(CUser, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=16,
        choices=[(role.value, role.value) for role in ClientRole.all()]
    )

    def __str__(self):
        return self.user.email
