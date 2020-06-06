print("Conversor de tempo!")
d = int(input("Quantos dias: "))
h = int(input("Quantas horas: "))
m = int(input("Quantos minutos: "))
s = int(input("Quantos segundos: "))
print(f" {d} dia(s), {h} hora(s), {m} minuto(s) e {s} segundo(s) São: {(d * 86400) + (h * 3600) + (m * 60) + (s * 1)} Segundos")

# pode ser tbm {(d * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + s}