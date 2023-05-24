print("=" *20)
print("PROGRESSÃO ARITMÉTICA(PA)")
print("=" *20)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
print(décimo)
for c in range(primeiro, décimo + razão, razão):
    print(c, end=" - ")
print("ACABOU!")