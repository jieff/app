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
	elif op == 2:
		subtrair()
	else:
		menu()
	

# SUBTRAIR
def subtrair():
	
	print(" ")
	num1 = float(input("Digite o primeiro número: "))
	print(" ")
	num2 = float(input("Digite o segundo número: "))
	result_subtracao = (num1 - num2)
	print(" ")
	print "                     o resultado da subtração é: ",result_subtracao
	print(" ")
	print("********************************************************************")
	
	retorno()

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
	retorno()

# Define o retorno para o menu
def retorno(): 
 	op = int(input('''

	               >> Para voltar ao menu principal tecle : 1

	               >> Para sair do aplicativo tecle       : 0
	
        **************************************************************************
	
	'''))


	if op == 1:
		menu()
	else:
		quit()
		

#Define metodo principal

if __name__ == '__main__':
    menu()
