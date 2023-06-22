from django.db import models
from .usuario import usuario

class familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    id_UserName = models.ForeignKey(usuario,related_name='Familiar', on_delete = models.CASCADE)
    parentesco= models.CharField('parentesco',max_length=30)
    correo = models.CharField('Especialidad',max_length=30)
    