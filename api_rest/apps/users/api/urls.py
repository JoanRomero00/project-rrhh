from django.urls import path
from .api import user_api_view, user_detail_api_view

urlpatterns = [
    path('users/', user_api_view, name='users_api_view'),
    path('users/<int:pk>/', user_detail_api_view, name='user_detail_api_view'),
]
