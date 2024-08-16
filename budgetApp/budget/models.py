from django.db import models

class Budget(models.Modle):
    name = models.CharField(max_length=100)
