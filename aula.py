inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

print("Múltiplos de 5 no intervalo:")

for i in range(inicio, fim + 1):
    if i % 5 == 0:
        print(i)