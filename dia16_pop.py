cliente = input("Digite o nome do cliente: ")

servicos = []

servico_1 = input("Digite o primeiro serviço: ")
servico_2 = input("Digite o segundo serviço: ")
servico_3 = input("Digite um serviço digitado por engano: ")

servicos.append(servico_1)
servicos.append(servico_2)
servicos.append(servico_3)

removido = servicos.pop()

print("Cliente:")
print(cliente)

print("Serviços finais:")
print(servicos)

print("Serviço removido:")
print(removido)
