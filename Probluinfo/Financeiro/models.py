from django.db import models
from Pessoas.models import Pessoas

# Create your models here.
class Caixa(models.Model):
    Entrada = 1
    Saida = 2

    TIPOS_CHOICES = (
        (Entrada,'Entrada'),
        (Saida,'Saída'),
    )

    tipo = models.CharField(max_length=1,choices=TIPOS_CHOICES, blank=False)
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    dt_lancamento = models.DateField(max_length=10, blank=False)
    id_pessoa_id = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Caixa'
    
    def __str__(self):
        return self.tipo
