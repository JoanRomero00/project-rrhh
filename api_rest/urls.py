from django.contrib import admin
from django.urls import path, include
from api_rest.apps.users.views import Login, Logout, UserToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.apps.users.api.urls')),
    path('api/', include('api_rest.apps.employees.api.routers')),
    path('refresh-token/',UserToken.as_view(), name = 'refresh_token'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout')
]
