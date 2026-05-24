from django.shortcuts import render
from .models import Usuario

# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # SALVAR OS DADOS DA TELA NO BANCO DE DADOS
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # EXIBIR TODOS OS USUÁRIOS JÁ CADASTRADOS EM UMA NOVA PAGINA
    usuarios = {
        'usuarios' : Usuario.objects.all()

    }
    # RETORNAR OS DADOS PARA A PAGINA DE LISTAGEM DE USUÁRIOS
    return render(request, 'usuarios/usuarios.html', usuarios)
