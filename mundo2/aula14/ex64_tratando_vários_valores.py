n = soma = 0
cont = -1
n = int(input("Digite um número: ")) # sem essa linha também funciona!
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número: "))
print(f"Você digitou {cont} números e a soma entre eles é de {soma}!")