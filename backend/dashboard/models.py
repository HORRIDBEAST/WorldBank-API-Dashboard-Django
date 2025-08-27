from django.db import models
from django.contrib.auth.models import User

class WorldBankData(models.Model):
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    indicator_code = models.CharField(max_length=50)
    indicator_name = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('country_code', 'indicator_code', 'year')