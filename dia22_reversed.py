cliente = input("Digite o nome do cliente: ")

servicos = []

servico_1 = input("Digite o primeiro serviço: ")
servico_2 = input("Digite o segundo serviço: ")
servico_3 = input("Digite o terceiro serviço: ")

servicos.append(servico_1)
servicos.append(servico_2)
servicos.append(servico_3)

servicos_invertidos = " | ".join(reversed(servicos))

print("Cliente:")
print(cliente)

print("Serviços na ordem original:")
print(servicos)

print("Serviços exibidos em ordem invertida:")
print(servicos_invertidos)

print("Lista original preservada:")
print(servicos)
