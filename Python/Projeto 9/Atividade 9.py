numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = i * numero
    print(f"{i:2} x {numero} = {resultado:3}")
