
# nome = "Alan" # Global

# def saudacao():
#     sobrenome = "Code" #Local
#     print(f"Olá, {nome} {sobrenome}")
 
# saudacao()

# def somar(n1, n2): # n1 e n2 são paremetros
#     print(f"A soma de {n1} e {n2} é {n1 + n2}")

#somar(6, 40) # 6 e 40 são argumentos

def formatar_real(valor):
    return f"R$ {valor:.2f}".replace(".", "X").replace(",", ".").replace("X", ",")

# Uso:
preco_hospedagem = 49.9
print(formatar_real(preco_hospedagem))  # Saída: R$ 49,90



