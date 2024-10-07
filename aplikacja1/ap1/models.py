from django.db import models

# Create your models here.
class Store(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)