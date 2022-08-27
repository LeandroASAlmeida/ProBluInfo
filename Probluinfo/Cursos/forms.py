
from django.forms import ModelForm
from Cursos.models import Cursos,Salas,Matriculas,Notas

# Create your models here.
class FormCursos(ModelForm):
    class Meta:
        model = Cursos
        fields = ['id','nm_curso','carga_horaria','vl_curso']
        db_table = 'Cursos'          

class FormSalas(ModelForm):
    class Meta:
        model = Salas
        fields = ['id','nm_sala','capacidade']  
        db_table = 'Salas'

class FormSalasAltera(ModelForm):
    class Meta:
        model = Salas
        fields = ['id','nm_sala','capacidade']  
        db_table = 'Salas'

class FormMatriculas(ModelForm):
    class Meta:
        model = Matriculas
        fields = ['id','dt_inicio','dt_fim','qtd_dias','qtd_horas','id_pessoa','id_curso','periodo','id_sala']   
        db_table = 'Matriculas'

class FormNotas(ModelForm):
    class Meta:
        model = Notas
        fields = ['id','nota_1','nota_2','nota_3','nota_4','media','id_matricula']
        db_table = 'Notas'
