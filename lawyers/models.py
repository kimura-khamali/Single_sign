from django.db import models

# Create your models here.
from users.models import User

class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firm = models.CharField(max_length=25)
    profile_image = models.ImageField(upload_to='lawyer_images/', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user} - {self.firm}"