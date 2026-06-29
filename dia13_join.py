cliente = input("Digite o nome do cliente: ")
servicos = input("Digite os serviços separados por vírgula: ")

servicos = servicos.split(",")

servicos_formatados = " | ".join(servicos)

print("Registro criado:")
print(cliente)

print("Serviços formatados:")
print(servicos_formatados)
