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
    id = int(input("digite o id do produto"))
    nome = input ("Digite o Nome Do Produto: ")
    quantidade = int(input("Digite a Quantidade: "))
    preco = float(input("Digite o Preco: "))

except ValueError:
    print("Digite o Valor Corretamente")

#montar o objeto
novo_produto = {
                "id": id,
                "nome": nome,
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





#modificar produto no json 
# id --> identificar
#pao da vo neuza - 1 
#pao dona benta - 2 

# ---------------modificar produto-----------------
#d_produto_modificar = int (input("digite o id para modificar"))
nova_quantidade = int (input("digite a nova quantidade"))
try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load (arquivo)
except FileNotFoundError: 
    print("arquivo nao encontrado")


produto_encontrado = False 
for produto in inventario: 
    if produto["id"] == id_produto_modificar:
         #colocamos a nova quantidade
        produto ["quantidade"] = nova_quantidade
        produto [" em_estoque"] = nova_quantidade > 0
        produto_encontrado = True
        break;
if not produto_encontrado:
    print (" o produto com o id informado nao foi encontrado")

else:
    with open ("loja.json", "w") as arquivo:
        json.dump (inventario, arquivo, indent = 4 )
    print ("o arquivo foi alterado com sucesso!!")



#xcluir produtos no json 
try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print ("arquivo nao encontrado")
novo_inventario = [ ]
produto_excluido = False
id_produto_excluir = int (input("digite o id do produto para excluir"))
for produto in inventario:
    if produto ["D"] != id_produto_excluir:
     #se o id for diferente, adicionamos a nova lista 
     novo_inventario.append (produto)
else:
    print ("produto removido com sucesso!!")
    produto_excluido = True
if not produto_excluido:
    print ("o id do produto nao foi encontrado")
else:
    with open ("loja.json", "W") as arquivo:
        json.dump (novo_inventario, arquivo, indent = 4)
    print ("o arquivo foi atualizado, prouto removido")
#listar produtos do arquivo json 
try:
    with open ("loja.json", "r") as arquivo:
        inventario = json.load (arquivo)
    if not inventario:
        print ("o arquivo esta vazio!")
    else:
        print ("____ lista de produtos no inventario ______")
        for produto in inventario:
            print (f"w __ produto {produto.get("id")}___")
            print (f"Nome:{produto.get("nome_produto","n/a")}")
            print (f"Preco:{produto.get("preco_unitario", 0):.2f}")
            print (f"Quantidade:{produto.get("quantidade", 0 )}unidades")
            print (f"Em estoque:{produto.get("em_estoque")}")
except FileNotFoundError:
    print ("arquivo nao encontrado")
