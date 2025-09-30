# {} -> chaves : definir um objeto -> ficha de cadastro
#                                     pessoa - nome , cpf, tell
#[] -> colchete: definir uma lista 
# chave/valor : chave descreve o valor
#                "telefone" "4499924-558774"
# sempre vai importar o json 


import json 
inventario = []
# lendo o arquivo
try:
    with open ("loja.json", "r") as arquivo: 
        inventario = json.load(arquivo)
except FileNotFoundError:
    print ("arquivo nao encontrado")
try:
    nome = input ("Digite o Nome Do Produto: ")
    quantidade = int(input("Digite a Quantidade: "))
    preco = float(input("Digite o Preco: "))

except ValueError:
    print("Digite o Valor Corretamente")

#montar o objeto
novo_produto = {"nome": nome,
                "quantidade": quantidade,
                "preco": preco,
                "em_estoque": quantidade > 0  #expressao verdadeira ou falso 
                }
                
                
                
#escrever o objeto no arquivo            
inventario.append (novo_produto)
with open ("loja.json", "w") as arquivo: 
    json.dump(inventario, arquivo, indent = 4 )
    #indent -> formatar o arquivo json 
print ("produto cadastrado com sucessso")