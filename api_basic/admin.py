from django.contrib import admin
from .models import Transaction
from .models import TransactionType

admin.site.register(Transaction)
admin.site.register(TransactionType)
