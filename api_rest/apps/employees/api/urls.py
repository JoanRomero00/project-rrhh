from django.urls import path
from .api import employee_api_view

urlpatterns = [
    path('employees/', employee_api_view, name='users_api_view'),
]