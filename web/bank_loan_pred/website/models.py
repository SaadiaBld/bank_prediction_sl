from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegister(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"