from django.shortcuts import render
from perfis.models import Perfil
# Create your views here.

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil("Flavio Almeida","flavio@flavio.com.br","22222","Caelum")

	if perfil_id == "2":
		perfil = Perfil("Romulo Henrique","romulo@romulo.com.br","1233443","Caelum")
		
	return render(request, 'perfil.html', {"perfil" : perfil})