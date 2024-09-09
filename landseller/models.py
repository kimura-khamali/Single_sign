from django.db import models
from lawyers.models import Lawyer
from users.models import User

class LandSeller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='landseller')
    lawyer = models.ForeignKey(Lawyer, on_delete=models.SET_NULL, null=True, blank=True, related_name='land_sellers')
    address = models.CharField(max_length=26)

    objects = models.Manager()


    def __str__(self):
        return f"{self.user} - {self.address}"


