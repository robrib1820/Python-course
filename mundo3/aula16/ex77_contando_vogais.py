palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar",
"trabalhar","mercado","programaor","futuo")

for p in palavras:
    print(f"\n Na palavra {p} temos", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ") 