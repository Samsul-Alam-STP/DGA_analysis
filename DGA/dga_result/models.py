from django.db import models

# Create your models here.
class DGA_Values(models.Model):
    hydrogen = models.FloatField(default=None, null=False)
    carbon_di_oxide = models.FloatField(default=None, null=False)
    carbon_monoxide = models.FloatField(default=None, null=False)
    ethylene = models.FloatField(default=None, null=False)
    ethane = models.FloatField(default=None, null=False)
    methane = models.FloatField(default=None, null=False)
    acetylene = models.FloatField(default=None, null=False)
    tdcg = models.FloatField(default=None, null=False)

