from django.db import models

class TransactionType(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(max_length = 100)
    description = models.CharField(max_length = 256)
        
class Transaction(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    type = models.ForeignKey(TransactionType, on_delete =models.RESTRICT,blank=True, null=True)
    description = models.CharField(max_length = 256)
    date = models.DateField(auto_now = True)

