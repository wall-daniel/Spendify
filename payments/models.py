from django.db import models


class Payment(models.Model):
    description = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    amount = models.FloatField(default=0)

