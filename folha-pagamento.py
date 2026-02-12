print("===================Folha de pagamento===================")
salario = float(input("Digite o salário do funcionário: "))
if salario <= 900:
    print("Isento de imposto de renda")
elif salario > 900 and salario <= 1500:
    imposto = salario * 0.05
    print(f"Imposto de renda: R$ {imposto:.2f}")
elif salario > 1500 and salario <= 2500:
    imposto = salario * 0.10
    print(f"Imposto de renda: R$ {imposto:.2f}")
else:
    imposto = salario * 0.20
    print(f"Imposto de renda: R$ {imposto:.2f}")