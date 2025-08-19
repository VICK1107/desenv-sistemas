#Crie uma lista de tarefas
#Adicione uma tarefa na lista 
#Adicione uma tarefa na posicao 2 da lista 
#remover a tarefa "lavar louca" da lista 
#Remover a tarefa da posicao 1 da lista 

"lavar loucas", "varrer a casa", "limpar a casa", "limpar o quarto", "lavar o banheiro"


tarefas = [] 
tarefas.append("lavar louças")
tarefas.append("varrer a casa")
tarefas.append("limpar a casa")
tarefas.append("limpar o quarto")
tarefas.append("lavar o banheiro")

print(tarefas) 

tarefas.insert(2, "varrer quintal")

print(tarefas)

tarefas.remove("lavar louças")

print(tarefas)

tarefas.pop(1)

print(tarefas)
