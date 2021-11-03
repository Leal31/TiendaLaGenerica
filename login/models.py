from django.db import models

# Create your models here.

class Usuario(models.Model):

    Usuario=models.CharField(max_length=255, null=True)

    Contraseña=models.CharField(max_length=255, null=True)
