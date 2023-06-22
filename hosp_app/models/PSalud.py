from tkinter import CASCADE
from django.db import models
from .usuario import usuario

class Personal_Salud(models.Model):

    id_PersonalSalud = models.AutoField(primary_key=True)
    id_UserName = models.ForeignKey(usuario,related_name='PSalud', on_delete = models.CASCADE)
    rol = models.CharField('Rol',max_length=30)
    especialidad = models.CharField('Especialidad',max_length=60)
    


