print("=============================================================")
print("===============Conversor de tempo para segundos===============")
print("=============================================================")

dias = int(input("Digite o número de dias: "))
print("=============================================================")
horas = int(input("Digite o número de horas: "))
print("=============================================================")
minutos = int(input("Digite o número de minutos: "))
print("=============================================================")
segundos = int(input("Digite o número de segundos: "))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print("=============================================================")
print("========================resultado============================")
print("=============================================================")
print("Dias:", dias, "Horas:", horas, "Minutos:", minutos, "Segundos:", segundos)
print("Total de segundos:", total_segundos, "segundos" )