try:
    print("Abrindo conexão com o banco de dados...")
    resultado = 10 / 2
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    # Este bloco sempre executa, havendo erro ou não
    print("Fechando conexão com segurança.")
