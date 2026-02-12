print ("1 idoso")
print ("2 gestante")
print ("3 cadeirante")
print ("4 nenhuma das anteriores")
resposta = int(input("Digite o número correspondente à sua condição: "))

if resposta == 1:
    print("Fila prioritária para idosos")
elif resposta == 2:
    print("Fila prioritária para gestantes")
elif resposta == 3:
    print("Fila prioritária para cadeirantes")
else:
    print("Fila comum")