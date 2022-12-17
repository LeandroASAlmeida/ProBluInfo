from django.forms import ModelForm
from Financeiro.models import Caixa

class FormCaixa(ModelForm):
    class Meta:
        model = Caixa
        fields = ['id','tipo','id_pessoa','descricao','valor','dt_lancamento']
        db_table = 'Caixa'