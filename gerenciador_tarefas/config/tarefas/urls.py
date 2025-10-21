from django.urls import path 
from . import views 
urlpatterns = [
    path ("", views.listar_tarefas, name = "lista_tarefas"),
    #detalhes da tarefa 
    #<int:tarefa_id> captura um numero do url
    path('<int:tarefa_id>/', views.detalhe_tarefa, name = 'detalhe_tarefa'),
]
