print("-=-" *20)
print("Analisador de triângulos")
r1 = float(input("Primeiro Seguimento "))
r2 = float(input("Primeiro Seguimento "))
r3 = float(input("Primeiro Seguimento "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima PODEM FORMAR trinângulo!")
else:
    print("Os seguimentos acima NÃO PODEM FORMAR triângulo!")
