"""Probluinfo URL Configuration
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from core import views
from ViewsProject import views
from .views import login

from Cursos.views import cadastra_cursos,cadastra_salas,cadastra_notas,cadastra_matriculas
from Cursos.views import lista_cursos,lista_salas,lista_notas,lista_matriculas
from Cursos.views import altera_cursos,altera_salas,altera_notas,altera_matriculas
from Cursos.views import exclui_cursos,exclui_salas


from Financeiro.views import cadastra_lancamentos
from Financeiro.views import lista_lancamentos
from Financeiro.views import altera_lancamentos


from Pessoas.views import cadastra_pessoas
from Pessoas.views import lista_pessoas
from Pessoas.views import altera_pessoas
from Pessoas.views import exclui_pessoas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login,name='login/'),


    # Path Altera
    path('altera-pessoas/<int:id>',altera_pessoas,name='altera-pessoas'),
    path('altera-cursos/<int:id>',altera_cursos,name='altera-cursos'),
    path('altera-salas/<int:id>',altera_salas,name='altera-salas'),
    path('altera-notas/<int:id>',altera_notas,name='altera-notas'),
    path('altera-matriculas/<int:id>',altera_matriculas,name='altera-matriculas'),
    path('altera-lancamentos/<int:id>',altera_lancamentos,name='altera-lancamentos'),

    # Path Cadastra
    path('cadastra-pessoas',cadastra_pessoas, name='cadastra-pessoas'),
    path('cadastra-cursos',cadastra_cursos, name='cadastra-cursos'),
    path('cadastra-salas',cadastra_salas, name='cadastra-salas'),
    path('cadastra-notas',cadastra_notas, name='cadastra-notas'),
    path('cadastra-matriculas',cadastra_matriculas, name='cadastra-matriculas'),
    path('cadastra-lancamentos',cadastra_lancamentos, name='cadastra-lancamentos'),

    # Path Lista
    path('lista-pessoas',lista_pessoas, name='lista-pessoas'),
    path('lista-cursos',lista_cursos, name='lista-cursos'),
    path('lista-salas',lista_salas, name='lista-salas'),
    path('lista-notas',lista_notas, name='lista-notas'),
    path('lista-matriculas',lista_matriculas, name='lista-matriculas'),
    path('lista-lancamentos',lista_lancamentos, name='lista-lancamentos'),

     # Path Exclui
    path('exclui-pessoas/<int:id>', exclui_pessoas,name='exclui-pessoas'),
    path('exclui-cursos/<int:id>', exclui_cursos,name='exclui-cursos'),
    path('exclui-salas/<int:id>', exclui_salas,name='exclui-salas'),


    path('accounts/',include('django.contrib.auth.urls')),
    path("",include('ViewsProject.urls')),

  
    # Path Reseta Senha
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
handler404 = 'core.views.pagina_inexistente'
handler400 = 'core.views.nao_autorizado'


