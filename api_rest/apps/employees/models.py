from django.db import models

from api_rest.apps.base.models import BaseModel
from api_rest.apps.users.models import User
# Create your models here.

class Employee(BaseModel):
    """Model definition for Employee."""

    # TODO: Define fields here
    name = models.CharField('Nombre', max_length=50, unique=False, blank=False, null=False)
    last_name = models.CharField('Apellido', max_length=50, unique=False, blank=False, null=False)
    dni = models.CharField('DNI', max_length=8, unique=True, blank=False, null=False)
    phone = models.CharField('Telefono', max_length=12, unique=False, blank=False, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario', null=True)
    birth_date = models.DateField('Fecha de Nacimiento', auto_now=False, auto_now_add=False)
    address = models.TextField('Dirección', blank=False, null=False)
    
    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of Employee."""
        return f'DNI: {self.dni} - {self.name} {self.last_name}'
