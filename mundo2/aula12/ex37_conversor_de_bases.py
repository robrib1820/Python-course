num = int(input("Digite um número inteiro: "))
print('''Escolha uma das abases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')
opção = int(input("Sua Opção: "))

if opção == 1:
    print(f"O {num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"O {num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"O {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção inválida. Tente novamente!")