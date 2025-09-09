#usando(lacos,funcao e try/except), crie um sistema para receber as 3 notas de um aluno e calcule a media anual se digitar algo sem ser numero tratar o erro

#usando(lista,funcao,lacos,try/except), voce devera criar uma lista com numeros e mensagens se for numero adicionar a uma lista a parte se for mensagem, tratar com o erro de tipo ao final, mostrat a lista so com os numeros


def receber_nota(indice):
    while True:
        try:
            nota = float(input(f"Digite a nota {indice} do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print(" A nota deve estar entre 0 e 10.")
        except ValueError:
            print(" Entrada inválida. Por favor, digite um número.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    print(" Sistema de Notas do Aluno\n")

    notas = []
    for i in range(1, 4):
        nota = receber_nota(i)
        notas.append(nota)

    media = calcular_media(notas)
    print(f"\n A média anual do aluno é: {media:.2f}")

    if media >= 7:
        print(" Situação: Aprovado!")
    elif media >= 5:
        print(" Situação: Recuperação.")
    else:
        print(" Situação: Reprovado.")

# Executa o programa
main()



exercicio 2
def filtrar_numeros(lista_mista):
    numeros = []
    for item in lista_mista:
        try:
            # Tenta converter o item para número (int ou float)
            numero = float(item)
            numeros.append(numero)
        except (ValueError, TypeError):
            # Se não for número, mostra uma mensagem (opcional)
            print(f"Ignorado (não é número): {item}")
    return numeros

# Lista com números e mensagens
lista_mista = [10, 'olá', 25.5, 'mundo', '123', 'erro', 42]

# Chama a função para filtrar os números
lista_numeros = filtrar_numeros(lista_mista)

# Mostra apenas os números encontrados
print("Lista apenas com números:")
print(lista_numeros)



#criar uma lista com cadastro de usuario
#cadastrar
#alterar
#executar
#listar
#usar(funcao,lista,try/exercept,lacos)


# Lista de usuários (cada usuário é um dicionário)
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario(lista):
    try:
        nome = input("Digite o nome do usuário: ").strip()
        email = input("Digite o email do usuário: ").strip()

        if not nome or not email:
            raise ValueError("Nome e email não podem estar vazios.")

        usuario = {"nome": nome, "email": email}
        lista.append(usuario)
        print(" Usuário cadastrado com sucesso!\n")

    except Exception as erro:
        print( "Erro ao cadastrar usuário: {erro}\n")

# Função para listar usuários
def listar_usuarios(lista):
    if not lista:
        print(" Nenhum usuário cadastrado.\n")
    else:
        print(" Lista de Usuários:")
        for i, usuario in enumerate(lista):
            print("{i}: Nome: {usuario['nome']}, Email: {usuario['email']}")
        print()

# Função para alterar usuário
def alterar_usuario(lista):
    try:
        listar_usuarios(lista)
        if not lista:
            return

        indice = int(input("Digite o índice do usuário que deseja alterar: "))
        
        if indice < 0 or indice >= len(lista):
            raise IndexError("Índice inválido.")

        novo_nome = input("Novo nome: ").strip()
        novo_email = input("Novo email: ").strip()

        if novo_nome:
            lista[indice]["nome"] = novo_nome
        if novo_email:
            lista[indice]["email"] = novo_email

        print(" Usuário alterado com sucesso!\n")

    except ValueError:
        print(" Digite um número válido para o índice.\n")
    except IndexError as erro:
        print(" {erro}\n")
    except Exception as erro:
        print(" Erro inesperado: {erro}\n")

# Função principal para executar o sistema
def executar():
    while True:
        print("==== Menu ====")
        print("1 - Cadastrar usuário")
        print("2 - Alterar usuário")
        print("3 - Listar usuários")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            alterar_usuario(usuarios)
        elif opcao == "3":
            listar_usuarios(usuarios)
        elif opcao == "4":
            print("🚪 Saindo do programa...")
            break
        else:
            print(" Opção inválida. Tente novamente.\n")

# Executar o programa
executar()
