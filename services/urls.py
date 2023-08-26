from django.urls import path
from .views import services_list, services_detail

urlpatterns = [
    path('services/', services_list, name='services-list'),
    path('services/<str:slug>', services_detail, name='services_detail')
]