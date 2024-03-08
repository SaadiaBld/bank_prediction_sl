from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_approved = models.BooleanField(default=False)
    # website_groups = models.ManyToManyField('auth.Group', related_name='website_user_groups')
    # website_user_permissions = models.ManyToManyField('auth.Permission', related_name='website_user_permissions')


class ModelApi(models.Model):
    Term = models.FloatField(default= 180)
    FranchiseCode = models.FloatField(default= 0)
    UrbanRural = models.FloatField(default= 0)
    RevLineCr = models.CharField(max_length=3, default= 'N')
    LowDoc = models.CharField(max_length=3, default= 'Y')
    GrAppv = models.IntegerField(default= 280000)
    SBA_Appv = models.IntegerField(default= 210000)
    NAICS_digit = models.IntegerField(default= 62)

