from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class usuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):

        user = self.create_user(
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class usuario(AbstractBaseUser, PermissionsMixin):
    
    id_username = models.BigAutoField(primary_key=True)
    username = models.CharField('Username',max_length=250,unique=True)
    password = models.CharField('Password', max_length = 250)
    perfil = models.CharField('Perfil', max_length = 250)
    nombre = models.CharField('Nombre', max_length = 250)
    apellidos= models.CharField('Apellido', max_length = 250)
    telefono = models.CharField('Telefono', max_length = 250)
    genero= models.CharField('Genero', max_length = 250)

    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = usuarioManager()
    USERNAME_FIELD = 'username'

