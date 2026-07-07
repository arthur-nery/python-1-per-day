cliente = input("Digite o nome do cliente: ")

servicos = []

servico_1 = input("Digite o primeiro serviço: ")
servico_2 = input("Digite o segundo serviço: ")
servico_3 = input("Digite o terceiro serviço: ")

servicos.append(servico_1)
servicos.append(servico_2)
servicos.append(servico_3)

print("Ordem original:")
print(servicos)

servicos.reverse()

print("Ordem invertida:")
print(servicos)
