from django.db import models

class Collection(models.Model):
    collection_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    collcover=models.CharField(max_length=1000)

# Create your models here.
