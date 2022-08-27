from django.urls import path
from ViewsProject.views import *

urlpatterns = [
    path('suporte/',suporte, name='suporte'),
    path('base/',base_pbi, name = "base-pbi"),
    path("",login, name="login"),
    path("login_view/",login_view, name="login-view"),
    path("sobre/",sobre, name="sobre"),
    path('recup-senha/',recup_senha, name ="recup-senha"),
    path('altera-senha/',altera_senha, name = "altera-senha"),
    path('atualizar-dados/',atualizar_dados, name="atualizar-dados")
]
