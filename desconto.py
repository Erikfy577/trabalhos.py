valor = int(input("Digite um valor: "))
desconto = int(input("Digite a porcentagem de desconto: "))

valor_desconto = valor * (desconto / 100)

print("Valor com desconto de", desconto, "%:", valor - valor_desconto) 