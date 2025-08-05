#desafio 
#pedir nome e senha do usuario 
#mostrar "bem vindo" quando acertar senha e o nome 
#apos, pedir o salario do usuario 
#mostrar salario anual
#se o salario  anual for maior que 100 mil mostrar mensagem "rico"



senha_correta = input("configure uma senha")
senha = input("digite sua senha")
nome = input("digite seu nome")
salario = float(input("digite seu salario"))


while senha != senha_correta:
    print("senha incorreta") 
    senha = input("digite sua senha correta")
print("senha correta")
print("bem-vindo", nome)

salarioanual = salario * 12
if (salarioanual > 100000): 
    print("rico")
