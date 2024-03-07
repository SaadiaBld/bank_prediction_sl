from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_approved = models.BooleanField(default=False)
    website_groups = models.ManyToManyField('auth.Group', related_name='website_user_groups')
    website_user_permissions = models.ManyToManyField('auth.Permission', related_name='website_user_permissions')


class ModelApi(models.Model):
    Term = models.FloatField()
    FranchiseCode = models.FloatField()
    UrbanRural = models.FloatField()
    RevLineCr = models.CharField(max_length=1)
    LowDoc = models.CharField(max_length=1)
    GrAppv = models.IntegerField()
    SBA_Appv = models.IntegerField()
    NAICS_digit = models.IntegerField()

