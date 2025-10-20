from django.shortcuts import render 
from .models import Tarefa 
from django.http import HttpResponse 

def listar_tarefas(request):
    tarefas_salvas = tarefas.objects.all()
    contexto = {
        "minhas tarefas": tarefas_salvas
        }
    return render (request, 'tarefas/lista.html', contexto )

