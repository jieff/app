# -*- coding: utf-8 -*-

# MENU PRINCIPAL

def menu():

    print (" ")
    print ("Bem Vindo ao PYCalculator 0.1.")
    print("")
    print ("")
    var = int(input('''Para calcular digite a tecla correspondente:
     ---------------------------
    | < 1 > Para Porcentagem.   |
    | < 2 > Para Soma           |
    | < 3 > Para Subtração      |
    | < 4 > Para Multiplicação  |
    | < 5 > Para Raiz Quadrada  |
    | < 6 > Para Raiz Cúbica    |
    | < 7 > Para Divisão        |
     ---------------------------

     '''))

    if var == 1:
        porcentagem()

    elif var == 2:
        soma()

    elif var == 3:
        multiplicacao()

    elif var == 4:
        multiplicacao()

    elif var == 5:
        raiz_quadrada()

    elif var == 6:
        raiz_cubica()

    elif var == 7:
        subtracao()

# PROCENTAGEM

def porcentagem():

    print (" ")
    inteiro = float( input("Agora, digite um numero para calcular a porcentagem:"))
    print("")
    porcentagem = float( input("Porcentagem a calcular?"))
    divisaon = 100
    divisao = float (divisaon)
    resultado = (inteiro * porcentagem / (divisao));
    print ("")
    print("O resultado é:\n\n\t", resultado)
    print("")
    print ("""Muito obrigado por utilizar nosso programa!
    Att,
    Lucas
    """)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal tecle 0



    '''))

    if var == 1:
        porcentagem()

    else:
        menu()

# SOMA

def soma():

    print("")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_soma = (numero_1 + numero_2)
    print (" ")
    print ("O resultado da soma é:\n\n\t", resultado_soma)

    var= int(input('''

    Para calcular novamente tecle: 2
    Para voltar ao menu principal tecle 0



    '''))

    if var == 2:
        soma()

    else:
        menu()

# SUBTRAÇÃO

def subtracao():

    print(" ")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_subtração = (numero_1 - numero_2)
    print (" ")
    print ("O resultado da subtração é:\n\n\t", resultado_subtração())
    var= int(input('''

    Para calcular novamente tecle: 3
    Para voltar ao menu principal tecle 0



    '''))

    if var == 3:
        subtracao()

    else:
        menu()

# MULTIPLICAÇÃO

def multiplicacao():

    print (" ")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_multiplicacao = (numero_1 * numero_2)
    print (" ")
    print ("O resultado da multiplicação é:\n\n\t", resultado_multiplicacao)

    var= int(input('''

    Para calcular novamente tecle: 4
    Para voltar ao menu principal tecle 0



    '''))

    if var == 4:
        multiplicacao()

    else:
        menu()

# RAIZ QUADRADA

def raiz_quadrada():

    print (" ")
    numero_1 = float(input("Digite o numero para calcular a raiz: "))
    resultado_raizquadrada = (numero_1 **(1/2))
    print (" ")
    print ("A raiz quadrada é:\n\n\t", resultado_raizquadrada)
    var= int(input('''

    Para calcular novamente tecle: 5
    Para voltar ao menu principal tecle 0



    '''))

    if var == 5:
        raiz_quadrada()

    else:
        menu()

# RAIZ CÚBICA

def raiz_cubica():

    print (" ")
    numero_1 = float(input("Digite o numero para calcular a raiz: "))
    resultado_raizcubica = (numero_1 **(1/3))
    print (" ")
    print ("A raiz cúbica é:\n\n\t", resultado_raizcubica)
    var= int(input('''

    Para calcular novamente tecle: 6
    Para voltar ao menu principal tecle 0



    '''))

    if var == 6:
        raiz_cubica()

    else:
        menu()

# DIVISÃO

def divisao():
    print("")
    numero_1 = float(input("Digite o primeiro numero: "))
    print (" ")
    numero_2 = float(input("Digite o segundo numero: "))
    resultado_divisao = (numero_1 / numero_2)
    print (" ")
    print ("O resultado da divisão é:\n\n\t", resultado_divisao)

    var= int(input('''

    Para calcular novamente tecle: 2
    Para voltar ao menu principal tecle 0



    '''))

    if var == 7:
        divisao()

    else:
        menu()


if __name__ == '__main__':
    menu()
