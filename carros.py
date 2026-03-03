from datetime import datetime

print("=== CONFIGURADOR DE CARROS PREMIUM+ ===")

# Data e hora
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M:%S")

# =========================
# BASE DE DADOS DOS CARROS
# =========================

carros = {
    "BMW": {
        "Série 1": {"potencia": "140 cv", "combustivel": "Gasolina", "0-100": "8.5s", "vel_max": "213 km/h"},
        "Série 3": {"potencia": "184 cv", "combustivel": "Gasolina", "0-100": "7.2s", "vel_max": "235 km/h"},
        "Série 5": {"potencia": "252 cv", "combustivel": "Gasolina", "0-100": "6.0s", "vel_max": "250 km/h"},
        "X1": {"potencia": "150 cv", "combustivel": "Diesel", "0-100": "9.3s", "vel_max": "205 km/h"},
        "X3": {"potencia": "190 cv", "combustivel": "Diesel", "0-100": "8.0s", "vel_max": "213 km/h"},
        "X5": {"potencia": "265 cv", "combustivel": "Diesel", "0-100": "6.5s", "vel_max": "230 km/h"},
    },
    "Audi": {
        "A1": {"potencia": "110 cv", "combustivel": "Gasolina", "0-100": "10.5s", "vel_max": "200 km/h"},
        "A3": {"potencia": "150 cv", "combustivel": "Gasolina", "0-100": "8.4s", "vel_max": "220 km/h"},
        "A4": {"potencia": "204 cv", "combustivel": "Diesel", "0-100": "7.1s", "vel_max": "240 km/h"},
        "A6": {"potencia": "265 cv", "combustivel": "Diesel", "0-100": "6.1s", "vel_max": "250 km/h"},
        "Q3": {"potencia": "150 cv", "combustivel": "Gasolina", "0-100": "9.2s", "vel_max": "210 km/h"},
        "Q5": {"potencia": "204 cv", "combustivel": "Diesel", "0-100": "7.6s", "vel_max": "222 km/h"},
    }
}

# =========================
# ESCOLHA DA MARCA
# =========================

print("\nEscolha a marca:")
print("1 - BMW")
print("2 - Audi")

marca_input = input("Digite o número da marca: ")

if marca_input == "1":
    marca = "BMW"
elif marca_input == "2":
    marca = "Audi"
else:
    print("Marca inválida!")
    exit()

# =========================
# ESCOLHA DO MODELO
# =========================

modelos = list(carros[marca].keys())

print("\nEscolha o modelo:")
for i in range(6):
    print(f"{i+1} - {modelos[i]}")

modelo_input = input("Digite o número do modelo: ")

if modelo_input.isdigit() and 1 <= int(modelo_input) <= 6:
    modelo = modelos[int(modelo_input)-1]
else:
    print("Modelo inválido!")
    exit()

# =========================
# ESCOLHA DO ANO
# =========================

anos = ["2018", "2019", "2020", "2021", "2022", "2023"]

print("\nEscolha o ano:")
for i in range(6):
    print(f"{i+1} - {anos[i]}")

ano_input = input("Digite o número do ano: ")

if ano_input.isdigit() and 1 <= int(ano_input) <= 6:
    ano = anos[int(ano_input)-1]
else:
    print("Ano inválido!")
    exit()

# =========================
# ESCOLHA DA COR
# =========================

cores = ["Preto", "Branco", "Cinzento", "Azul", "Vermelho", "Prata"]

print("\nEscolha a cor:")
for i in range(6):
    print(f"{i+1} - {cores[i]}")

cor_input = input("Digite o número da cor: ")

if cor_input.isdigit() and 1 <= int(cor_input) <= 6:
    cor = cores[int(cor_input)-1]
else:
    print("Cor inválida!")