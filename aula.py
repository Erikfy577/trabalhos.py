# Lendo os números
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
# Mostrando valores originais
print("\nValores originais:")
print(f"x = {x}")
print(f"y = {y}")
# Trocando os valores
x, y = y, x
# Mostrando valores trocados
print("\nValores após a troca:")
print(f"x = {x}")
print(f"y = {y}")