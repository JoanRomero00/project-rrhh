from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api_rest.apps.employees.models import Employee
from api_rest.apps.employees.api.serializers import EmployeeSerializer


@api_view(['GET','POST'])
def employee_api_view(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many = True)
        return Response(employees_serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        employees_serializer = EmployeeSerializer(data = request.data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return Response({'message':'Empleado Creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(employees_serializer.errors, status = status.HTTP_400_BAD_REQUEST)