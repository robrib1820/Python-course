peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (M)"))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc <18.5:
    print("Você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print("Parabéns! Você está na faixa de PESO NORMAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPESO")
elif imc >= 30 and imc <40:
    print("Você está em OBESIDADE!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA!")
