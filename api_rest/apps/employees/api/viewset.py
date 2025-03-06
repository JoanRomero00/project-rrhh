import datetime
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from api_rest.apps.employees.api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
        
    def list(self, request):
        employee_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(employee_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        # send information to serializer
        serializer = self.serializer_class(data = request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Empleado creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            employee_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if employee_serializer.is_valid():
                employee_serializer.save()
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        employee = self.get_queryset().filter(id=pk).first() # get instance        
        if employee:
            employee.state = False
            employee.delete_date = datetime.datetime.now
            employee.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)