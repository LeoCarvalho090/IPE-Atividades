import datetime
#Atividade Nota Fiscal

# Defina os detalhes da empresa
nome_empresa = input("Digite o nome da empresa")
endereco_empresa = input("Digite o endereço da empresa")
cnpj_empresa = input("Digite o CNPJ da empresa")

# Defina os detalhes do 
nome_cliente = input("Digite o nome do cliente")
endereco_cliente = input("Digite o endereço do Cliente")
cpf_cliente = input("Digite o cpf do cliente")

# Defina os detalhes da compra
numero_nf = input("Digite o numero da NF")
data_emissao = datetime.datetime.now()
descricao_produto = input("Digite a descrição do produto")
quantidade = int(input("Digite a quantidade"))
preco_unitario = float(input("Digite o valor do produto"))

# Calcule o valor total
total = quantidade * preco_unitario

# Imprima a nota fiscal
print("===================================")
print("          NOTA FISCAL")
print("===================================")
print(f"Nome da Empresa: {nome_empresa}")
print(f"Endereço: {endereco_empresa}")
print(f"CNPJ: {cnpj_empresa}")
print("\n")
print(f"Nome do Cliente: {nome_cliente}")
print(f"Endereço: {endereco_cliente}")
print(f"CPF: {cpf_cliente}")
print("\n")
print(f"Número da Nota Fiscal: {numero_nf}")
print(f"Data de Emissão: {data_emissao}")
print("\n")
print("==== ITENS DA COMPRA ====")
print(f"Descrição do Produto: {descricao_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço Unitário: R${preco_unitario:.2f}")
print(f"Total: R${total:.2f}")
print("\n")
print("===================================")