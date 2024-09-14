lista = []

entrada = int(input('Calculo Fibonacci, entre com um número: '))

def calculoFibonacci(n):
    a, b = 0, 1
    for i in range(n):
        lista.append(a)
        a, b = b, a + b


def exibirNaTela():
    for item in lista:
        print(f"{item}", end=" ")

    if entrada in lista:
        print('\nNúmero pertence ao resultado do calculo fibonacci.')
    else:
        print(f'\nNúmero {entrada} não pertence ao resultado do calculo de fibonacci.')

    

calculoFibonacci(entrada)
exibirNaTela()
