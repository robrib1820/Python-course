nome = str(input("Qual é o seu nome? "))
if nome == "Robson":
    print("Que nome bonito")
elif nome == "Maria" or nome == "João" or nome =="Pedro":
    print("Seu nome é bem popular no Brasil")
elif nome in "Ana Claúdia Jéssica Juliana":
    print("Belo nome Feminino!")
else:
    print("Seu nome é be normal!")
print(f"Tenha um bom dia {nome}")