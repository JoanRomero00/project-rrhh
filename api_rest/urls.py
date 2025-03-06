from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.apps.users.api.urls')),
    path('api/', include('api_rest.apps.employees.api.routers')),
]
