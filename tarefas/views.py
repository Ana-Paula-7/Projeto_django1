from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/adicionar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')

    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form':form})

def deletar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/deletar_tarefa.html', {'tarefa':tarefa})
