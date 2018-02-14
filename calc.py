# -*- coding: utf-8 -*-


#Menu Principal

def menu():
	
	print(" ")
	print("Bemvindo a Calculadora")
	print(" ")
	print(" ")
	op = int(input(''' Digite o numero da operação desejada:

	***************************
	| 1 - Soma                |
	| 2 - Subtraçao           |
	| 3 - Divisao             |
	| 4 - Multiplicaçao       |
	***************************

	'''))

#Metodo de escolha das operações

	if op == 1:
		soma()
	else:
		menu()

# SOMA

def soma():

	print(" ")
	num1 = float(input("Digite o primeiro numero: "))
	print (" ")
	num2 = float(input("Digite o segundo numero: "))
	resultado_soma = (num1 + num2)
	print (" ")
	print "O resultado da soma eh:",resultado_soma

	op = int(input('''

	Para calcular novamente tecle: 1
	Para voltar ao menu principal tecle 2
	Para sair do aplicativo tecle 0
	'''))


	if op == 2:
		menu()
	elif op == 1:
		soma()
	else:
		quit()
		

#Define metodo principal

if __name__ == '__main__':
    menu()
