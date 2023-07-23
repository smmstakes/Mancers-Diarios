from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_User = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=30)


class Diario(models.Model):
    id_Diario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)

