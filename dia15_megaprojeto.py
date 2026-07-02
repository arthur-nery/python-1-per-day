print("Megaprojeto Dia 15")
print("Registro simples de atendimento")

cliente = input("Digite o nome do cliente: ")
servicos_digitados = input("Digite os serviços separados por vírgula: ")
valor_pago = input("Digite o valor pago: ")
status = input("Digite o status do pagamento: ")
quantidade_servicos = input("Digite a quantidade de serviços realizados: ")


cliente = cliente.strip()
servicos_digitados = servicos_digitados.strip()
valor_pago = valor_pago.strip()
status = status.strip()
quantidade_servicos = quantidade_servicos.strip()
quantidade_servicos = int(quantidade_servicos)

status_minusculo = status.lower()

status = status.upper()

valor_pago = valor_pago.replace(",", ".")
valor_pago = float(valor_pago)
valor_pago_texto = str(valor_pago)

servicos_separados = servicos_digitados.split(",")

servicos = []

servico_1 = servicos_separados[0].strip()
servico_2 = servicos_separados[1].strip()

servicos.append(servico_1)
servicos.append(servico_2)

servicos_formatados = " | ".join(servicos)

print("Resumo do atendimento")
print("Cliente:")
print(cliente)

print("Quantidade de caracteres no nome:")
print(len(cliente))

print("Serviços:")
print(servicos_formatados)

print("Valor pago:")
print(valor_pago)

print("Tipo do valor pago:")
print(type(valor_pago))

print("Status:")
print(status)

print("Status em letras minúsculas:")
print(status_minusculo)

print("Quantidade de serviços:")
print(quantidade_servicos)

print("Valor pago em texto:")
print("R$ " + valor_pago_texto)
