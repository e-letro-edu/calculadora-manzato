#fazendo uma calculadora.
#Qual a operação que ele vai utilizar.

def somar(n1,n2):
    return n1+n2

def diminuir(n1,n2):
    return n1-n2

def dividir(n1,n2):
    return n1/n2

def multiplicar(n1,n2):
    return n1*n2

while True:
    print('----------------- Bem vindo a nossa calculadora -----------------')
    print('|                                                               |')
    print('|                    Calculadora do MANZATO                     |')
    print('|                                                               |')
    print('-----------------------------------------------------------------')
    operacao = input('Escreva a sua operação (+, -, /, *): ')

    soma = 1
    subtracao = 2
    multiplicacao = 3
    divisao = 4

    print("Informe os dois valores com que deseja trabalhar!")
    numero_1 = float(input("Qual é o valor 1: "))
    numero_2 = float(input("Qual é o valor 2: "))

    #Qual o resultado das operações.
    if operacao == 1:
        resultado = somar(numero_1,numero_2) 
        print("O resultado da sua equação é:", resultado)

    elif operacao == 2:
        resultado = diminuir(numero_1,numero_2)
        print("O resultado da sua equação é:", resultado)

    elif operacao == 3:
        resultado = dividir(numero_1,numero_2)
        print("O resultado da sua equação é:", resultado)

    elif operacao == 4:
        resultado = multiplicar(numero_1,numero_2)
        print("O resultado da sua equação é:", resultado)