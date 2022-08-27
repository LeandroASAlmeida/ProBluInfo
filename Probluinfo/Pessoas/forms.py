from django.forms import ModelForm
from Pessoas.models import Pessoas

class FormPessoas(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['id','cpf','dt_nascimento','celular','fone_res','nm_resp','id_perfil','username','password','first_name','last_name','email']
        db_table = 'Pessoas'

class FormPessoasAltera(ModelForm):
    class Meta:
        model = Pessoas
        fields = ['id','cpf','dt_nascimento','celular','fone_res','nm_resp','id_perfil','first_name','last_name','email','is_active']
        db_table = 'Pessoas'