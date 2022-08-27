from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Perfis(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'Perfis'

    def __str__(self):
        return self.descricao

class Pessoas(AbstractUser):
    cpf = models.CharField(max_length=14, blank=False, unique=True)
    dt_nascimento = models.DateField(max_length=10, blank=False)
    celular = models.CharField(max_length=15, blank=True, unique=True)
    fone_res = models.CharField(max_length=15, blank=True)
    nm_resp = models.CharField(max_length=100, blank=True)
    dt_alteracao = models.DateField(auto_now=True)
    id_perfil = models.ForeignKey(Perfis, on_delete=models.PROTECT)

    class Meta:
        db_table = 'Pessoas'

    def __str__(self):
        return self.first_name
    