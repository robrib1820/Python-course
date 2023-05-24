from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
# print(f"O computador escolher {itens[computador]}")1
jogador = int(input("Qual é a sua jogada?"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*15)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*15)

if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print("EMPATOU")
    elif jogador == 1:
        print("jOGADOR VENCE")
    elif jogador ==2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATOU")
    elif jogador ==2:
        print("jOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA!")

elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print("jOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador ==2:
        print("EMPATOU")
    else:
        print("JOGADA INVÁLIDA!")
