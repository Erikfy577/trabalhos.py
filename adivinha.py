import os

numero_secreto = input("Digite um número de 1 a 9 para seu colega adivinhar: ")

os.system('cls' if os.name == 'nt' else 'clear')

print("--- HORA DE ADIVINHAR ---")

acertou = False

while not acertou:
    palpite = input("Tente adivinhar o número: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if palpite == numero_secreto:
        print("Boa! Você tem o dom, acertou em cheio! ")
        acertou = True  
    else:
        print("Errou feio, errou rude! Tente novamente.")

print("parabens, você acertou o número secreto! O número era:", numero_secreto)