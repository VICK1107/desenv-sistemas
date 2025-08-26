#Exceptions em Python são erros que ocorrem durante a execução de um programa, sendo usadas para sinalizar situações excepcionais que podem interromper o fluxo normal do código.
 #A principal forma de tratar esses erros é utilizando os blocos try except

#Exemplos de Exceptions comuns

ValueError:Ocorre quando uma função recebe um argumento com o tipo certo, mas valor inapropriado
    1 * = int("hello")
#neste exemplo, tentamos converter a string "hello" para um inteiro, o que gera um ValueError
ZeroDivisionError: Ocorre quando tentamos dividir um numero por ZeroDivisionError
    resultado = 10 / 0
#aqui, tentamos dividir 10 por 0, gerando um ZeroDivisionError
IndexError: Ocorre quando tentamos acessar um índice que nao existe em uma lista 
    Lista = [1,2,3]
    Print(lista[5])
#neste caso, tentamos acessar o índice 5 de uma lista que só possui 3 elementos, gerando um IndexError     

#10 Tipos de exemplos de uso em try/except comuns

#1. ZeroDivisionError - Divisão por zero
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero!")

#Explicação:
O código tenta dividir 10 por 0, o que resulta em um erro de divisão por zero (ZeroDivisionError). Usando o try/except,
    podemos capturar esse erro e exibir uma mensagem amigável, em vez de o programa falhar abruptamente.



#2. ValueError - Valor inválido para conversão
try:
    x = int("abc")
except ValueError:
    print("Valor inválido para conversão!")

#Explicação:
Aqui, estamos tentando converter a string "abc" para um número inteiro, o que não é possível. O erro gerado é um ValueError, 
    e ao capturá-lo, podemos informar ao usuário que o valor não pode ser convertido para um número.



#3. IndexError - Acessando um índice que não existe
try:
    lista = [1, 2, 3]
    x = lista[5]
except IndexError:
    print("Índice fora do alcance!")
    
#Explicação:
O código tenta acessar o elemento de índice 5 em uma lista que só possui 3 elementos. Isso gera um IndexError,
    que é tratado para evitar que o programa trave. A mensagem ajuda a entender que o índice solicitado não existe.



#4. KeyError - Acessando uma chave que não existe em um dicionário
try:
    dicionario = {"a": 1, "b": 2}
    x = dicionario["c"]
except KeyError:
    print("Chave não encontrada!")


#Explicação:
Estamos tentando acessar a chave "c" em um dicionário que não a contém. Isso gera um KeyError.
    Capturamos o erro para evitar uma falha no programa e fornecemos uma mensagem útil sobre a chave inexistente.



#5. FileNotFoundError - Tentando acessar um arquivo que não existe
try:
    with open("arquivo_inexistente.txt", "r") as f:
        conteúdo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")


#Explicação:
Aqui, estamos tentando abrir um arquivo chamado "arquivo_inexistente.txt", que não existe. Um FileNotFoundError é gerado,
     e ao tratá-lo, podemos exibir uma mensagem indicando que o arquivo não foi encontrado, evitando que o programa trave.



#6. TypeError - Operação inválida entre tipos diferentes
try:
    x = "10" + 10
except TypeError:
    print("Não é possível somar uma string com um número!")

#Explicação:
Aqui estamos tentando somar uma string com um número, o que não é permitido em Python. Isso gera um TypeError. Capturamos o erro para informar que essa operação não é válida.



#7. AttributeError - Tentando acessar um atributo que não existe em um objeto
try:
    x = "texto".não_existe()
except AttributeError:
    print("Método ou atributo não encontrado!")


#Explicação:
Estamos tentando chamar um método chamado não_existe() em uma string. Como esse método não existe, um AttributeError é gerado. 
    Capturamos o erro para que o programa não quebre, avisando que o atributo ou método não foi encontrado.


#8. NameError - Tentando acessar uma variável não definida
try:
    print(variavel_inexistente)
except NameError:
    print("Variável não definida!")

#Explicação:
Aqui estamos tentando acessar uma variável que nunca foi definida. Isso gera um NameError, e com o try/except, 
    conseguimos capturar o erro e informar que a variável não foi definida.


#9. ImportError - Tentando importar um módulo que não existe
try:
    import modulo_inexistente
except ImportError:
    print("Módulo não encontrado!")

#Explicação:
Neste código, tentamos importar um módulo chamado modulo_inexistente, que não existe. O ImportError é gerado, 
    e podemos capturá-lo para avisar que o módulo não foi encontrado, evitando que o programa trave.


#10. OverflowError - Número excedendo o limite de dados
try:
    x = 1e1000  # Um número muito grande
except OverflowError:
    print("O número é muito grande!")

#Explicação:
Estamos tentando criar um número muito grande (mais do que o Python pode lidar), o que resulta em um OverflowError. 
    O código captura esse erro e exibe uma mensagem indicando que o número é muito grande para ser processado.











#Tipos de exemplos de uso em try/except usando funcao e lista nos exemplos 

#Exemplo 1: Acessando um índice de lista que pode não existir
#Este exemplo tenta acessar um índice em uma lista, tratando erros caso o índice não exista.

def acessar_lista(lista, indice):
    try:
        item = lista[indice]
    except IndexError:
        print(f"Erro: O índice {indice} está fora do alcance da lista.")
    else:
        print(f"O item na posição {indice} é: {item}")
    finally:
        print("Tentei acessar um índice da lista.")

# Exemplo de uso
#lista = [1, 2, 3, 4, 5]
#acessar_lista(lista, 10)  # Índice que não existe
#acessar_lista(lista, 2)   # Índice válido

#Explicação:
#O try tenta acessar o índice da lista.
#O except captura o erro caso o índice seja inválido.
#O finally sempre executa, independentemente do erro ou sucesso.


#Exemplo 2: Manipulando números em uma lista
#Aqui, a função tenta dividir cada número em uma lista, tratando erros como divisão por zero ou tipos incompatíveis.

def dividir_lista(lista):
    resultados = []
    for numero in lista:
        try:
            resultado = 100 / numero  # Tentando dividir por cada número
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")
            resultados.append(None)  # Adiciona None se ocorrer erro
        except TypeError:
            print("Erro: A lista contém valores não numéricos.")
            resultados.append(None)  # Adiciona None para valores inválidos
        else:
            resultados.append(resultado)
    return resultados

# Exemplo de uso
#lista_numeros = [10, 0, 20, 'a', 5]
#resultados = dividir_lista(lista_numeros)
#print(f"Resultados das divisões: {resultados}")

#Explicação:
#O try tenta realizar a divisão.
#O except captura os erros de divisão por zero e tipo incompatível.
#A função retorna uma lista de resultados, com None para os casos com erro.

#Exemplo 3: Verificando se todos os itens de uma lista são inteiros
#Este exemplo verifica se todos os elementos de uma lista podem ser convertidos para inteiros, utilizando uma função que tenta realizar a conversão e trata possíveis erros.

def verificar_lista(lista):
    inteiros = []
    for item in lista:
        try:
            inteiro = int(item)  # Tentando converter para inteiro
        except ValueError:
            print(f"Erro: '{item}' não é um número válido.")
            inteiros.append(None)  # Adiciona None se não for possível converter
        else:
            inteiros.append(inteiro)
    return inteiros

# Exemplo de uso
#lista_de_itens = ["10", "20", "abc", "30", "45.6"]
#inteiros_convertidos = verificar_lista(lista_de_itens)
#print(f"Lista de inteiros: {inteiros_convertidos}")

#Explicação:
#O try tenta converter cada item para um número inteiro.
#O except captura o erro caso o item não seja um número válido.
#A função retorna uma nova lista com os valores convertidos ou None para os itens que não puderam ser convertidos.



