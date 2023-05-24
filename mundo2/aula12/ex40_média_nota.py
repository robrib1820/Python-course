n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira nota: "))
média =  (n1 + n2) / 2
if média < 5.0:
    print(f"Sua nota foi {média}. REPROVADO!")
elif média < 6.9:
    print(f"Sua nota foi {média}. RECUPERAÇÃO")
else:
    print(F"Sua nota foi {média}. APROVADO!")