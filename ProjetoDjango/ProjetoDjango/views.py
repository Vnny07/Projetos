from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

def cadastro_tarefas(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        prioridade = request.POST.get('prioridade')
        usuario_id = request.POST.get('usuario')

        if descricao and setor and prioridade and usuario_id:
            usuario = Usuario.objects.get(id=usuario_id)  # Obtém o usuário selecionado
            Tarefa.objects.create(
                descricao=descricao,
                setor=setor,
                prioridade=prioridade,
                usuario=usuario
            )
            return redirect('cadastro_tarefas')
        else:
            return HttpResponse("Erro: Todos os campos são obrigatórios.")

    # Recupera os usuários cadastrados para exibir no combobox
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro_tarefas.html', {'usuarios': usuarios})

def cadastro_usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        if nome and email:
            Usuario.objects.create(
                usu_nome=nome,
                usu_email=email
            )
            return redirect('cadastro_usuarios')
        else:
            return HttpResponse("Erro: Todos os campos são obrigatórios.")

    # Aqui é onde passamos os usuários cadastrados para o template
    usuarios = Usuario.objects.all()  # Recupera os usuários no banco
    return render(request, 'cadastro_usuarios.html', {'usuarios': usuarios})

def index(request):
    return render(request, 'website/_layouts/index.html')

def cadastro_usuarios(request):
    return render(request, 'website/_layouts/cadastro_usuarios.html')

def cadastro_tarefas(request):
    return render(request, 'website/_layouts/cadastro_tarefas.html')

def gerenciar_tarefas(request):
    return render(request, 'website/_layouts/gerenciar_tarefas.html')