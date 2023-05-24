cont = homem = mulher = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    continuar = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if idade > 18:
        cont += 1
    if sexo == "M":
        homem += 1
    if sexo =="F":
        if idade < 20:
            mulher += 1
    if continuar == "N":
        break
        
print(f"O número de pessoas cadastradas com idade maior de 18 anos foi {cont}!")
print(f"O número de homens cadastrados foi {homem}.")
print(f"Das mulheres cadastradas somente {mulher} tem menos de 20 anos.")
