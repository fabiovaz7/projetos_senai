# def formatar_real_replace(valor):
#     texto = f"R$ {valor:,.2f}" #padrão EUA: 1,234.56
#     texto = texto.replace(",", "X")
#     texto = texto.replace(",", "X")  
#     texto = texto.replace("X", ".") 
#     return texto

# #Uso 
# preco = 1234.5
# print(formatar_real_replace(preco)) # R$ 1.234,50

# Parametros com valor padrão (default)
# def saudacao(nome, mensagem="Bem vindo!"):
#     print(f"Olá, {nome}! {mensagem}")

# saudacao("Ana")
# saudacao("Bob", "Bom dia!")

# # Argumentos nomeados (keyword args)
# def cria_usuario(nome, idade, admin=False):
#     print(f"{nome} | {idade} anos | admin = {admin}")

# cria_usuario(idade=20, nome="Carol")
# cria_usuario("Dan", 25, admin=True)

# def criar_perfil(nome, idade, cidade):
#     print(f"{nome}, {idade} anos, {cidade}")

# # Chamadas com argumentos nomeados (ordem não importa)
# criar_perfil(cidade="Curitiba", nome="Chupson", idade=40)
# criar_perfil(nome="Ana", idade=25, cidade="São Paulo")

# # Função com quantidade variável de argumentos
# def somar_tudo(*numeros):
#     return sum(numeros)

# # Exibindo os resultados
# print(somar_tudo(1, 2))
# print(somar_tudo(1, 2, 3, 4))
# print(somar_tudo(20, 30))





# Criando um dicionário 

# produto = {"nome": "Teclado", "preco":150, "em_estoque": True}

# # Acessando um valor 
# print(produto["nome"])

# # Modificando um valor
# produto["preco"] = 135.00

# # Adicionando um novo par 
# produto["quantidade"] = 10

# print(produto)



def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    
# Criamos um dicionário vazio para armazenar as entradas
info_usuario = {}

print("Digite as informações (ou 'sair' na chave para encerrar): ")

while True:
    chave = input("Nome do campo (ex: Profissão): ")
    if chave.lower() == 'sair':  # corrigido aqui
        break 
    valor = input(f"Valor para {chave}: ")
    info_usuario[chave] = valor

# Usamos ** para desempacotar o dicionário com argumentos 
exibir_info(**info_usuario)