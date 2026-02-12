nota = (float(input("Digite a nota do aluno: ")))
presenca = (float(input("Digite a porcentagem de presença do aluno (0 a 1): ")))

if nota >= 7.0 and presenca >= 0.75:
    print("Aprovado")
elif nota < 7.0 and presenca >= 0.75:
    print("Reprovado por nota")
elif nota >= 7.0 and presenca <= 0.75:
    print("Reprovado por presença")
else:
    print("Reprovado por nota e presença insuficiente")