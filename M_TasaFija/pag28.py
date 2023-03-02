#Ejercicio de la pagina 28 MATEMATICAS FINANCIERAS
from tabulate import tabulate

#solicitamos los datos y los guardamos en variables flotantes
N = float(input("Ingrese el numero de años de vida util: "))
S = float(input("Ingrese el valor de salvamento: "))
B = float(input("Ingrese el valor de la depreciacion acumulada al final de la vida util: "))

C = S + B

d = 1 - (S / C)**(1 / N)

Dt = [0]
Da = [0]
V = [0]
V[0] = C

for i in range(1, int(N+1)):
    V.append(C * (1-d)**i)
    Dt.append((V[i-1]) * d)
    Da.append(Da[i-1] + Dt[i])

#imprimimos la tabla
table = []
for i in range(0, int(N+1)):
    table.append([i, d ,Dt[i], Da[i], V[i]])

print(tabulate(table, headers=["Año", "Tasa", "Depreciacion", "Depreciacion acumulada", "Valor del activo"], tablefmt="fancy_grid"))
print("Datos finales")
print("Costo del activo: ", C)
print("Vida util del activo: ", N)
print("Tasa de depreciacion anual: ", d)
print("Valor de salvamento: ", S)

#graficamos la tabla
import matplotlib.pyplot as plt
plt.plot(Dt, label="Depreciacion")
plt.plot(Da, label="Depreciacion acumulada")
plt.plot(V, label="Valor del activo")
plt.legend()
plt.show()

