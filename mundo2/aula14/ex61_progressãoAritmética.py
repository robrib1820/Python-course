print("=" *20)
print("PROGRESSÃO ARITMÉTICA(PA)")
print("=" *20)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} →", end=" ")
    termo += razão
    cont += 1
print("Fim")