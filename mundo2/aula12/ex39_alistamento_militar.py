from datetime import date
atual = date.today().year
ano = int(input("Ano de nascimento: "))
sexo = str(input("Masculino / Feminino: "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {atual}!")
if idade == 18 and sexo == "Masculino":
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18 and sexo == "Masculino":
    anos = 18 - idade
    print(f"Você ainda não tem 18 anos. Ainda faltam {anos} anos para o alistamento!")
    print(f"Seu alistamento será em {atual + anos}.")
elif idade > 18 and sexo == "Masculino": 
    anos = idade - 18
    print(f"Você já deveria ter se alistado há {anos} anos!")
    print(f"Seu alistamento foi em {atual - anos}.")
else: 
    print("O serviço militar para você não é obrigatório!")
print()