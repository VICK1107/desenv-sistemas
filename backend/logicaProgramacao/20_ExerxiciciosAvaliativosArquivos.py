                               #EXERCICIO 1
#Eu como dono de uma padaria, quero um sistema onde eu possa cadastrar meus produtos alem de poder listar, alterar em caso de errar, e excluir quando acabar o estoque.
# Quero tambem que tenha um menu onde eu possa ver as opcoes possiveis

#Cadastrar produto, Listar produtos, Alterar produto, Excluir produto, Sair do sistema 

def carregarArquivo():
    try:
        with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo não encontrado")

def menu():
    carregarArquivo()
    print("=== Menu Padaria === \n")
    print("1 -cadastro \n")
    print("2 -lista \n")
    print("3 - alterar produto \n")
    print("4 - excluir produto \n")
    print("5 - sair")
    opcao = input ("digite a opcao desejada: ")


    while opcao != "sair":
        
        if opcao == "1":
            cadastro()
    
        elif opcao == "2":
            lista() 

        elif opcao == "3":   
            alterar_produto()

        elif opcap == "4":
            excluir()

        elif opcao == "sair" :
            print("saindo...")   
    

def cadastro():   
    lista = []
    nome = input ("digite o nome do produto: ")
    lista.append(nome)

    with open('padaria.txt', 'w') as arquivo: 
        arquivo.writelines(lista)
        break

def lista():
    lista = []
    with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()
            print(lista)
    

def alterar_produto():
    lista = []
    produto_alterar = input("Digite o nome do produto para alterar:")
    with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()

    for produto in lista:
        if produto == produto_alterar:
            novo_nome = input("Digite o nome alterado: ")
            produto = novo_nome

    with open('padaria.txt', 'w') as arquivo: 
        arquivo.writelines(lista)
    
def excluir():
    lista = []
    produto_excluir = input("Digite o nome do produto para excluir:")
    with open('padaria.txt', 'r') as arquivo: 
            lista = arquivo.readlines()

    for produto in lista:
        if produto != produto_excluir:
            lista.append(produto)

    with open('padaria.txt', 'w') as arquivo: 
        arquivo.writelines(lista)

menu()



   



with open('arquivo.txt', 'r') as file: dados = file.readlines()
# # ESCREVER: with open('arquivo.txt', 'w') as file: file.writelines(dados)





    
                              #EXERCICIO 2
#Sou dono de uma concessionaria e vi o sistema do dono da padaria. Gostaria de um sistema igual para meus carros.


                             #EXERCICIO 3
#Explique porque quando tenho mais de um atributo(variavel), torna-se dificil/complicado o uso de arquivos.txt para guardar as informacoes



