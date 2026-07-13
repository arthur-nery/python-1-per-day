cliente = input("Digite o nome do cliente: ")

servicos = []

servico_1 = input("Digite o primeiro serviço: ")
servico_2 = input("Digite o segundo serviço: ")
servico_3 = input("Digite o terceiro serviço: ")

servicos.append(servico_1)
servicos.append(servico_2)
servicos.append(servico_3)

print("Cliente:")
print(cliente)

print("Serviços registrados:")
print(servicos)

print("Limpando lista de serviços...")

servicos.clear()

print("Serviços após limpar:")
print(servicos)
