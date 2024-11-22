from django.urls import path
from . import views

urlpatterns = [
    path("payment_request/", views.payment_request_veu, name="payment_request"),
    path("hotel_room/", views.hotel_room_veu, name="hotel_room_veu"),
    path("payment_request_update_statys/<int:application_id>", views.payment_request_update_statys_veu, name="payment_request_update_statys"),
    path("dashboard/", views.dashboard_viu, name="dashboard"),
    path("update_statys/<int:room_id>/", views.update_status, name="hotel_room_update_status"),
    path("tour_end_payments/", views.tour_end_payments_viu, name="tour_end_payments"),
]
