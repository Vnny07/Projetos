from django.shortcuts import render

def index(request):
    return render(request, 'website/_layouts/index.html')

def cadastro_usuarios(request):
    return render(request, 'website/_layouts/cadastro_usuarios.html')

def cadastro_tarefas(request):
    return render(request, 'website/_layouts/cadastro_tarefas.html')

def gerenciar_tarefas(request):
    return render(request, 'website/_layouts/gerenciar_tarefas.html')