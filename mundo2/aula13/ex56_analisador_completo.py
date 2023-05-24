somaIdade = 0
maiorIdadeHomem = 0
nomeVelho = 0
totmulher20 = 0
for p in range(1, 5):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: ").strip())
    sexo = str(input("SEXO [M/F]: ").strip())
    somaIdade += idade
    if p == 1 and sexo in "Mn":
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Mn" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in "Ff" and idade < 20:
         totmulher20 += 1
médiaIdade = somaIdade / 4
print(f"A média de idade do grupo é de {médiaIdade} anos.")
print(f"O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos.")