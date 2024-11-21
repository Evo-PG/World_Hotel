from django.urls import path
from . import views

urlpatterns = [
    path("payment_system/<int:pk>", views.payment_system_veu, name='payment_system'),
    path("my_payment_applications/", views.my_payment_applications_veu, name="my_payment_applications")
]
