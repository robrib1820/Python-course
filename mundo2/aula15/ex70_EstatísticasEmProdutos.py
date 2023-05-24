print('''LOJA SUPER BARATÃO''')
total = totmil = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço R$: "))
    cont += 1
    total += preço
    if preço >1000:
        totmil += 1
    if cont == 1: #or preço < menor: Poderia ser feito assim para simplificar o código com o else abaixo!
        menor = preço
        barato = produto
    else: 
        if preço < menor:
            menor = preço
            barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("FIM DO PROGRAMA"))

print(f"O valor total dos produtos é R${total:.2f}.")
print(f"Temos {totmil} produtos custando mais de mil reais.")
print(f"O produto mais barato foi o {barato} que custa R${menor:.2f}")