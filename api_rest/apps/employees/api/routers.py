from rest_framework.routers import DefaultRouter
from api_rest.apps.employees.api.viewset import EmployeeViewSet

router = DefaultRouter()

router.register(r'employees',EmployeeViewSet,basename = 'employees')

urlpatterns = router.urls