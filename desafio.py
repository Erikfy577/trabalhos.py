dias_totais = int(input("Digite a quantidade de dias do mês: "))
horas_diarias = 16

dias_uteis = 0
for dia in range(dias_totais):
    dia_da_semana = dia % 7  
    if dia_da_semana < 5:
        dias_uteis += 1

horas_totais = dias_uteis * horas_diarias
minutos = horas_totais * 60
segundos = minutos * 60
milissegundos = segundos * 1000

print(f"\n--- Resultado para {dias_totais} dias ---")
print(f"Dias úteis calculados: {dias_uteis}")
print(f"Horas: {horas_totais} h")
print(f"Minutos: {minutos:,} min")
print(f"Segundos: {segundos:,} s")
print(f"Milissegundos: {milissegundos:,} ms")