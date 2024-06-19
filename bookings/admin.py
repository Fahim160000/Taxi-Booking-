from django.contrib import admin

# Register your models here.

from.models import TaxiDetails,Customer,PaymentReciept

admin.site.register(TaxiDetails)
admin.site.register(Customer)
admin.site.register(PaymentReciept)