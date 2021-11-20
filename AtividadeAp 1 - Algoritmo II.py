"""Escrever um algoritmo que lê o número de identificação de um aluno
as 3 notas obtidas nas 3 verificações e a média dos exercícios (ME)
que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7 """

print("Olá aluno! Digite seu numero de identificação para obter as notas dos exercicios.")
print("  ")

while True:
    try:
        id = int(input("Numero de identificação: "))
        if not 1 <= id <= 1000:
            raise ValueError("Tente novamente usando numeros de 1 a 1000!")
    except ValueError as t:
            print("Numero invalido!", t)
    else:
        break

print("-------------------")
nota1 = int(input("Digite a nota do exercicio 1: "))
nota2 = int(input("Digite a nota do exercicio 2: "))
nota3 = int(input("Digite a nota do exercicio 3: "))
ME = int(nota1 + nota2 + nota3)/3
MA1 = int(nota1 + nota2)*2
MA2 = (MA1 + nota3)*3
MA = (MA2 + ME)/7

print("-------------------")
print("-------------------")
print(" - Numero de identificação do aluno:", int(id))
print(f" - Notas: Nota1: {nota1}, Nota2: {nota2}, Nota3: {nota3}")
print(f" - Média dos exercicios: {ME:.2f}")
print(f" - Media de aproveitamento: {MA:.2f}")
print("-------------------")
print("-------------------")

if MA >= 6:
    print(f"Resultado do aluno ID: {id}: APROVADO!")
else:
    print(f"Resultado do aluno ID: {id}: REPROVADO!")
