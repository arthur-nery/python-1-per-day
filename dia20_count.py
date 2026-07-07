cliente = input("Digite o nome do cliente: ")

servicos = []

servico_1 = input("Digite o primeiro serviço: ")
servico_2 = input("Digite o segundo serviço: ")
servico_3 = input("Digite o terceiro serviço: ")

servico_1 = servico_1.strip().lower()
servico_2 = servico_2.strip().lower()
servico_3 = servico_3.strip().lower()

servicos.append(servico_1)
servicos.append(servico_2)
servicos.append(servico_3)

servico_contar = input("Digite o serviço que deseja contar: ")
servico_contar = servico_contar.strip().lower()

quantidade = servicos.count(servico_contar)

print("Cliente:")
print(cliente)

print("Serviços registrados:")
print(servicos)

print("Quantidade encontrada:")
print(quantidade)
