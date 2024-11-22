from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_viu, name="index"),
    path('ditail/<int:pk>/', views.ditail_viu, name="ditail"),
    path('create_hotel_room/', views.add_hotel_room, name="create_hotel_room"),
    path('create_category/', views.add_category, name="create_category"),
    path('add_services/', views.add_services, name="add_services"),
    path('event_list/', views.event_list_viu, name="event_list"),
]
