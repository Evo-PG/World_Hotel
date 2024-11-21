from django.contrib import admin
from .models import PaymentMethod, HotelPaymentApplication

admin.site.register(PaymentMethod)
admin.site.register(HotelPaymentApplication)
