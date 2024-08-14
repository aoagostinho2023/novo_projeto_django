from django.shortcuts import render
from .models import  Usuario
from django.http import HttpResponse
from django.core.management import call_command

def run_migrations(request):
    call_command('run_migrations')
    return HttpResponse('Migrations complete.')


# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvando os dados no DB
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Trazer dados contidos no DB
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #carregar pg com os dados
    return render(request, 'usuarios/usuarios.html', usuarios)

