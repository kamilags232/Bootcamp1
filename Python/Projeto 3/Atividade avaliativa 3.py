soma = 0
def somar_valores(a,b,c):
    return a + b + c
def main():
    valor1 = int(input("Digite o primeiro valor inteiro: "))
    valor2 = int(input("Digite o segundo valor inteiro: "))
    valor3 = int(input("Digite o terceiro valor inteiro: "))
    resultado = somar_valores(valor1, valor2, valor3)
    print("A soma dos três valores é:", resultado)
main()


