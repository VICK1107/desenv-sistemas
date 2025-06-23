idade = int(input("digite sua idade: "))

if (idade >=18):
    print("voce e maior de idade.")
elif (idade <18):
    print("voce e menor de idade.")


nota =int(input("digite sua nota:" ))
if (nota >=80):
    print("parabens.")
elif (nota <80 and nota >60):
    print("pode melhorar.")
elif (nota <60):
    print("recuperacao.")