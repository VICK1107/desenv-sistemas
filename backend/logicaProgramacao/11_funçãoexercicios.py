# CRIE UMA FUNCAO QUE VALIDE SE A SENHA ESTA CORRETA - DESAFIO 

# CRIE UMA FUNCAO QUE FACA A MEDIA DE 3 VALORES 
def media (num1,num2,num3):
    media = (num1 + num2 + num3) / 3
    print ("media:", media) 
media(3,2,1)

# CRIE UMA FUNCAO QUE CALCULE O IMPOSTO ANUAL DO SEU SALARIO
def imposto (salario):
    salarioanual = salario * 12 
    print ("seu salarioanual e: ", salarioanual)
 
    if (salario  >= 10000):
        imposto = 0.22 * salario 

    elif (salario <= 7000): 
        imposto = 0.22 * salario

    print ("seu imposto mensal e:" ,  imposto)
imposto (10000)
