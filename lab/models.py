from django.db import models

# Create your models here.
SEX = (('M', "Masculino"),
       ('F', "Femenino"),)

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=45)
