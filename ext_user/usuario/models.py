from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserPerfil(AbstractUser):
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.username