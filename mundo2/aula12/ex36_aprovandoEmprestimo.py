casa = float(input("Qual é o valor da casa? R$ "))
salário = float(input("Qual é seu salário? R$"))
anos = int(input("Quantos anos você quer pagar? "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f"Para pagar uma casa de R${casa:.2F} em {anos} anos a prestação será de R${prestação:.2F}")
if prestação <= mínimo:
    print("Empréstimo pode ser CONDEDIDO!")
else:
    print("Empréstimo NEGADO!")
print()