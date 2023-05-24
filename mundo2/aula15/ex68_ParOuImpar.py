from random import randint
v = 0
while True:
    jogador = (int(input("Diga um valor: ")))
    computador = randint(0, 11)
    total = computador + jogador 
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou ímpar? [P/I]")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {total}")
    print("Deu PAR" if total % 2 == 0 else "Deu ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU")
            v += 1
        else: 
            print("Você PERDEU!")
            break

    elif tipo == "I":
        if total % 2 == 1:
            print("Você GANHOU!")
            v += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {v} vezes.")