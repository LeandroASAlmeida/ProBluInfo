from enum import auto
from locale import locale_encoding_alias
from django.db import models
from Pessoas.models import Pessoas

# Create your models here.
class Cursos(models.Model):
    nm_curso = models.CharField(max_length=50,blank=False,unique=True)
    carga_horaria = models.DecimalField(default=1,max_digits=3,decimal_places=0,blank=False)
    vl_curso = models.DecimalField(default=1.000 ,max_digits=5,decimal_places=3,blank=False)

    class Meta:
        db_table = 'Cursos'

    def __str__(self):
        return self.nm_curso
            
class Salas(models.Model):
    nm_sala = models.CharField(max_length=50, blank=False, unique=True)
    capacidade = models.DecimalField(max_digits=3, decimal_places=0 ,blank=False)

    class Meta:
        db_table = 'Salas'
    
    def __str__(self):
        return self.nm_sala

class Matriculas(models.Model):
    Matutino = 1
    Vespertino = 2
    Noturno = 3
    
    PERIODOS_CHOICES = (
    (Matutino,'Matutino'),
    (Vespertino,'Verpertino'),
    (Noturno,'Noturno'),
    )
    
    dt_inicio = models.DateField(blank=False)
    dt_fim = models.DateField(blank=False)
    qtd_dias = models.DecimalField(max_digits=3,decimal_places=0,blank=False)
    qtd_horas = models.DecimalField(max_digits=3,decimal_places=0,blank=False)
    periodo = models.IntegerField(blank=False,choices=PERIODOS_CHOICES)
    id_sala = models.ForeignKey(Salas,on_delete=models.PROTECT)
    id_curso = models.ForeignKey(Cursos,on_delete=models.PROTECT)
    id_pessoa = models.ForeignKey(Pessoas,related_name='pessoas',on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'Matriculas'
    
    def __str__(self):
        return self.id_pessoa

class Notas(models.Model):
    id_matricula = models.ForeignKey(Matriculas,blank=False,on_delete=models.PROTECT)
    nota_1 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_2 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_3 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    nota_4 = models.DecimalField(max_digits=3,decimal_places=2,blank=False)
    media = models.DecimalField(max_digits=3,decimal_places=2)

    class Meta:
        db_table = 'Notas'

    def __str__(self):
        return self.id_matricula
    


    