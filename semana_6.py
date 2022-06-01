# -*- coding: utf-8 -*-
"""Semana 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZaOPR9puMbh4Lf25liLNSJv30KR89q4
"""

# def fatorial(numero):
#   if numero == 0:
#     return 1

#   fat = 1
#   for i in range(numero, 0, -1):
#     fat *= i
#   return fat

# numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
# fat = fatorial(numero)
# print(f"O fatorial de {numero} é {fat}")

# def fatorial(numero):
#     if numero == 0:
#         return 1
 
#     return numero * fatorial(numero - 1)
 
# numero = int(input("Digite um número inteiro para calcular seu fatorial: "))
# fat = fatorial(numero)
# print(f"O fatorial de {numero} é {fat}")

# def media(*numeros):
#   soma = 0
#   for numero in numeros:
#     soma += numero
#   return soma / len(numeros)

# resultado = media(2, 5, 9, 4, 11)
# print(f"O valor da média é {resultado}")

# def fatorial(numero):

#   """
#   Calcula o fatorial de um número

#   :parametro numero: número-base para o cálculo do fatorial
#   :return: resultado do cálculo do fatorial
#   """

#   if numero == 0:
#     return 1

#   fat = 1
#   for i in range(numero, 0, -1):
#     fat *= i
#   return fat

# def media(*numeros):

#   """
#     Calcula a média dos números passados para a função
#   :parametro numero: lista de numeros
#   :return: valro da media calculada
#   """

#   soma = 0
#   for numero in numeros:
#     soma += numero
#   return soma / len(numeros)

# resultado = media(2, 5, 9, 4, 11)
# print(f"O valor da média é {resultado}")

def receber_dados_contato():
    nome = str(input("Digite o nome do contato: "))
    telefone = int(input("Digite o telefone do contato: "))
    return nome, telefone

def inserir(agenda):
    contato = receber_dados_contato()
    if contato[0] in agenda:
      if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ").upper().strip()[0] == "N":
        return False
    agenda[contato[0]] = contato[1]
    return True

def remover(nome, agenda):
    if nome in agenda:
      del agenda[nome]
      return True
    else:
      return False

def menu():
    print("*** Agenda Telefônica ***")
    print("1. Inserir contato")
    print("2. Remover contato")
    print("3. Sair")
    return int(input("Escolha uma das opções: "))

agenda = {}
while True:
    op = menu()
    if op == 1:
      if inserir(agenda):
          print("Contato cadastrado com sucesso")
          print(agenda)
      else:
        print("Operação não realizada")
    elif op == 2:
        nome = str(input("Digite o nome a ser removido: "))
        if remover(nome, agenda):
            print("Contato removido!")
            print(agenda)
        else:
            print("Operação não realizada.")
    else:
      break