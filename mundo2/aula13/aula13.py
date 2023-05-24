# for x in range(0, 7, 4):
#     print(x)
# print("FIM")
# n = int(input("Digite um número: "))

# for x in range(0, n+1, 2):
#     print(x)



# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for x in range(i, f+1, p):
#     print(x)
# print("Fim")
s = 0
for x in range(0, 4):
    n = int(input("Digite um número: "))
    # s = s + n
    s += n
print(f"O somatório de todos os valores é {s}")