números = ("Zero", "Um", "Dois","Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez",
"Onze","Doze","Treza","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
# while num < 0 or num > 20:
#     print("Digite CORRETAMENTE!")
#     num = int(input("Digite um número entre 0 e 20: "))
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <=20:
        break
while True: 
    resp = str(input("Quer continuar? [S/N] "))
    if resp == "N":
        break
    else:
        num = int(input("Digite um número entre 0 e 20: "))
print(f"Você digitou o número {números[num]}")