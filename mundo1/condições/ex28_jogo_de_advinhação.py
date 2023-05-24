from random import randint
from time import sleep
computador = randint(0, 5)
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-"*20)
# print(f"Pensei no número {computador}") Número que o computador pensou!

jogador = int(input("Em que número pensei? ")) 
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabéns, você conseguiu me vencer!!")
else:
    print(f"Ganhei! Eu pensei no número {computador} e não no {jogador}!")
