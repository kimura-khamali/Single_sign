from django.db import models

# Create your models here.

from users.models import User
from lawyers.models import Lawyer

class LandBuyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='land_buyer') 
    lawyer = models.ForeignKey(Lawyer, on_delete=models.SET_NULL, null=True, blank=True, default='some_default_lawyer')
    address = models.CharField(max_length=30)

    objects = models.Manager()
    def __str__(self):
        return f"{self.user}"