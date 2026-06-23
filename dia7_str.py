cliente = input("Digite o nome do cliente: ")
valor = input("Digite o valor pago: ")

valor = float(valor)

print("Tipo antes de usar str():")
print(type(valor))

valor = str(valor)

print("Tipo depois de usar str():")
print(type(valor))

print("Registro final:")
print(cliente)
print(valor)
