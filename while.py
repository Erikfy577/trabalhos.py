while True:
    print("\n--- Sistema de Empréstimo Bancário ---")
    
    try:
        renda = float(input("Informe sua renda mensal: "))
        idade = int(input("Informe sua idade: "))
        nome_limpo_input = input("Possui nome limpo? (S/N): ").strip().upper()
        nome_limpo = True if nome_limpo_input == 'S' else False
        
        if idade > 75:
            print("\nStatus: REPROVADO (Regra de seguro: idade superior a 75 anos).")
        
        elif (nome_limpo and renda > 0) or (renda > 2000 and idade > 21):
            print("\nStatus: APROVADO!")
            
        else:
            print("\nStatus: REPROVADO (Requisitos mínimos não atingidos).")

    except ValueError:
        print("\nErro: Por favor, insira valores numéricos válidos.")
        continue

    continuar = input("\nDeseja consultar outro perfil? (S/N): ").strip().upper()
    if continuar != 'S':
        break

print("\nSistema encerrado. Até logo!")