from django.shortcuts import  render, get_object_or_404,redirect

def login(request):
    return render(request, 'login.html')

def post_delete(request):
	post = get_object_or_404()
	post.delete()
	return redirect(request,'base_pbi.html')

def pagina_inexistente(request, exception):
    return render(request, 'pagina_inexistente.html')

def nao_autorizado(request, exception):  # precisa ser exception
	return render(request, 'nao_autorizado.html')
