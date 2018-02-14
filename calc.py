# -*- coding: utf-8 -*-


#Menu Principal

def menu():
	
	print("***************************************************************** ")
	print(" ")
	print("                ..:: Bemvindo a Calculadora ::..")
	print(" ")
	print(" ")
	
	op = int(input('''      Digite o número da operação desejada:

	***************************
	| 1 - Soma                |
	| 2 - Subtração           |
	| 3 - Divisão             |
	| 4 - Multiplicação       |
	| 0 - Sair
	***************************
	
	'''))
	
	print "***************************************************************** "

#Metodo de escolha das operações

	if op == 1:
		soma()
	elif op == 0:
		quit()
	else:
		menu()

# SOMA

def soma():

	print(" ")
	num1 = float(input("Digite o primeiro número: "))
	print (" ")
	num2 = float(input("Digite o segundo número: "))
	resultado_soma = (num1 + num2)
	print (" ")
	print "                     O resultado da soma é: ",resultado_soma
	print(" ")
	print("*******************************************************************")
	op = int(input('''

	               >> Para calcular novamente tecle       : 1

	               >> Para voltar ao menu principal tecle : 2

	               >> Para sair do aplicativo tecle       : 0
	
**************************************************************************
	
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
