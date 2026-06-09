def se(condicao, valor_se_verdadeiro, valor_se_falso):
    return(valor_se_verdadeiro if condicao else valor_se_falso)

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("José", 94),
    ("Pedro", 70),
    ("Ricardo", 91),
    ("Bruno", 56),
    ("Bruna", 54),
    ("Silas", 51),
    ("Patrícia", 36),
    ("Tatiana", 82),
    ("Roseane", 36),
    ("Rebeca", 62),
    ("Carlos", 65),
    ("Marcos", 73),
    ("Adriana", 91),
    ("Adriano", 32)
]
print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-" * 38)

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO 🟢 ", se(nota>= 50, "RECUPERAÇÃO 🟡 ", "REPROVADO 🔴 "))

    print(f"{nome} {nota} {situacao}")

print("-" * 38)

print("\n --- Boletim Escolar ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    if nota >= 70:
        print(f"{nome} {nota} Aprovado")
        aprovados = aprovados + 1 
    elif nota >= 50:
        print(f"{nome} {nota} Recuperação")
        recuperacao = recuperacao + 1 
    else:
        print(f"{nome} {nota} Reprovado")
        reprovados = reprovados + 1 

print("-" * 38)
print(f"Total de alunos: {len(alunos)}")
print(f"Total de aprovados: {aprovados}")
print(f"Total de alunos recuperação: {recuperacao}")
print(f"Total de alunos reprovados: {reprovados}")

    