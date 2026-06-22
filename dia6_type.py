cliente = input("Digite o nome do cliente: ")
valor = input("Digite o valor pago: ")

print("Tipo do cliente:")
print(type(cliente))

print("Tipo do valor antes da conversão:")
print(type(valor))

valor = float(valor)

print("Tipo do valor depois da conversão:")
print(type(valor))
