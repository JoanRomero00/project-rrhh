from rest_framework import serializers
from api_rest.apps.employees.models import Employee
from api_rest.apps.users.api.serializers import UserSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = '__all__'