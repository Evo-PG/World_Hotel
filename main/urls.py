from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_viu, name="index"),
    path('ditail/<int:pk>/', views.ditail_viu, name="ditail")
]
