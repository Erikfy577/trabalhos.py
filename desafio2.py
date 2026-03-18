print("--- Desafio 1 ---")
vetor_reais = [10.5, 20.0, 5.5, 8.2, 12.0, 4.3, 7.8, 15.1, 3.9, 6.7]
soma = sum(vetor_reais)
media = soma / len(vetor_reais)

print("Vetor:", vetor_reais)
print("Soma:", soma)
print("Média:", round(media, 2))


print("\n--- Desafio 2 ---")
vetor_inteiros = [25, 12, 54, 8, 31, 2, 19]
maior = vetor_inteiros[0]
menor = vetor_inteiros[0]

for num in vetor_inteiros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Vetor:", vetor_inteiros)
print("Maior:", maior)
print("Menor:", menor)


print("\n--- Desafio 3 ---")
vetor_usuario = []
pares = 0

for i in range(8):
    num = int(input("Digite um número: "))
    vetor_usuario.append(num)
    if num % 2 == 0:
        pares += 1

print("Vetor:", vetor_usuario)
print("Pares:", pares)