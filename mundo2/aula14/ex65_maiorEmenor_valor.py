# resp = "S"
# total = 0
# maior = 0
# menor = 0
# while resp in "Ss":
#     n = int(input("Digite um número: "))
#     total += n
#     média = total / 2
#     if n > maior:
#         maior = n
#     if n > menor:
#         n = menor

#     resp = str(input("Quer Continuar ? [S/N] ")).upper().strip()
# print(f"A média dos números digitados é {média}")
# print(f"Dentr os números digitados o menor é o {menor} e o maior é o {maior}")
resp = "S"
soma = quant = média = 0
while resp in "Ss":
    n = int(input("Digite um número: "))
    soma += n
    quant+= 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("Quer Continuar ? [S/N] ")).upper().strip()
média = soma / quant
print(f"Você digitou {quant} números e a média deles é {média}.")
print(f"Dentre os números digitados o menor número é o {menor} e o maior número é o {maior}")