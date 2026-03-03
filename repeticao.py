#contador = 0
#while (contador <= 100):
#    print("contador =", contador)
#    contador = contador + 1 

continuar = "s"

while continuar == "s":
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    soma = n1 + n2
    print("Resultado:", soma)
    
    continuar = input("Deseja continuar? (s/n): ").lower()

print("Programa encerrado.")