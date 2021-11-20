# Exemplo de comando de entrada básica
import time
import timeit
import webbrowser
from timeit import *
from time import *
from os import *
from tkinter import *
import tkinter.messagebox
from webbrowser import *

while True:
    try:
        nome = str(input("Digite seu nome: "))
        if nome.isdigit():
            raise ValueError("Tente novamente utilizando somente letras!")
    except ValueError as l:
        print("Nome invalido!", l)
        print("Verifique se seu nome contem mais de 3 caracteres!")
    else:
        break

print(nome, "seu nome foi salvo com sucesso!")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if not 0 <= idade <= 110:
            raise ValueError("Tente novamente utilizando somente numeros de 0 a 110!")
    except ValueError as n:
        print("Idade invalida!", n)
    else:
        break

print("Sua idade foi salva com sucesso!")

print("Nome: " + nome)
print("Idade: " + str(idade) + " Anos.")
