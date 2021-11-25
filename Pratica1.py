# Esse código tem por finalidade:
# 1- Solicitar o nome do usuario - Se caso o nome não seja composto por caracteres(a-z) retornará um erro.
# 2- Solicitar a idade do usuario - Se caso a idade não seja composta por digitos(0-110) retornará um erro.

while True:
    try:
        nome = str(input("Digite seu nome: "))
        if nome.isdigit() or len(nome) < mincaracter or len(nome) > maxcaracter:
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
