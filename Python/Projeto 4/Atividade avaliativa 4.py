#Função que verifica se uma pessoa é maior de idade
def verificar_maioridade(idade):
    return idade >= 18
def main():
    idade = int(input("Digite sua idade: "))
    if verificar_maioridade(idade):
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
main()
