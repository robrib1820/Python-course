soma = 0
cont = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        # print(x, end=" ")
        soma += x
        cont = cont + 1
print(f"A soma de todos os {cont} valores solicitados é {soma}")
