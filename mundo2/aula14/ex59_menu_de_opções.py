from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa
    ''')
    opção = int(input(">>>>>>>> Qual é a sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma}.")
    elif opção == 2:
        produto = n1 * n2
        print(f"O resultado de {n1} vezes {n2} é {produto}.")
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"O maior número entre {n1} e {n2} é o {maior}.")
    elif opção == 4:
        print("Informe os números novamente!")
        n1 = int(input("Primeiro número:"))
        n2 = int(input("Segundo número: "))

    elif opção == 5:
        print("Finalisando...")
    else:
        print("Opção inválida! Tente novamente.")
    
    print("=-=" *10)
    sleep(2)
print("Fim do programa. Volte sempre!")
