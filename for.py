import os
frase = input("Digite uma frase: ")

os.system('cls' if os.name == 'nt' else 'clear')

total_vogais = 0

vogais_referencia = "aeiouAEIOU"

for letra in frase:  
    if letra in vogais_referencia:
        total_vogais += 1

print("=================Contador de vogais na frase=================")
print(f"A frase '{frase}' possui um total de {total_vogais} vogais.")
print("=============================================================")