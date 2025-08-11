#CRIAR FUNCAO DE OPCOES E PEDIR A OPCAO DESEJADA DO CLIENTE 
#CRIAR FUNCAO DE DEPOSITO 
#CRIAR UMA FUNCAO PARA SAQUE 
#CRIAR UMA FUNCAO DE VER O SALDO 
#AO DIGITAR SAIR ENCERRAR O PROGRAMA 

saldo = 0 

def menu():
    print("===Menu de opcoes === \n")
    print("1 -depositar \n")
    print("2 -saque \n")
    print("3 - saldo \n")
    print("4 - sair \n")
    opcao =imput ("digite a opcao desejada")
    
     while opcao != "sair":
        
        
     if opcao =="1":
        depositar(saldo)
    
    elif opcao == "2":
        saque(saldo) 

    elif opcao == "3":   
        verSaldo(saldo)

    elif opcao == "sair" 
        print("saindo...")   


def depositar(saldo):   
    valor = input ("digite o valor do deposito: ")
    saldo += valor 


def saque(saldo):
    valor = input("digite seu saque: ")
    saldo -= valor

def  verSaldo(saldo):
    print("seu saldo e: ", saldo)


    