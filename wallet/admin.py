from django.contrib import admin
from .models import *


class DetailsAdmin(admin.ModelAdmin):
    list_display = ["balance", "balance1", "transactions", "total_sent", "total_received", "total_received1", "private_key", "public_key", "address", "live_bitcoin_price", "live_bitcoin_price1", "balance_usd", "total_sent_usd", "total_received_usd"]
    list_filter = ["balance", "transactions", "total_sent", "public_key", "address",]

admin.site.register(Details, DetailsAdmin)