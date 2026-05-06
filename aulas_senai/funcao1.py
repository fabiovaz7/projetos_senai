
def calcular_media(nota1, nota2, nota3) :
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media
# Programa principal (Fora da função)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

resultado = calcular_media(n1, n2, n3)

print("Média final: ", resultado)