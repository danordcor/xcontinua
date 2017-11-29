from django.contrib import admin
from .models import Estudiante

# Register your models here.
admin.site.site_header = 'Integración Continua, Entrega Continua y Despliegue Continuo'
admin.site.register(Estudiante)
