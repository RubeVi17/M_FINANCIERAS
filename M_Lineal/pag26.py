from tabulate import tabulate

# Datos
C = 13850
S = C * 0.1
n = 8
d = 0.05

# Calcular valores
dt = [0]
dat = [0]
vt = [0]
vt[0] = C
for i in range(1,n):
    dt.append(vt[i-1] * d)
    dat.append(dat[i-1] + dt[i])
    vt.append(C-dat[i])

table = []
for i in range(n):
    table.append([i,dt[i],dat[i],vt[i]])

print(tabulate(table, headers=["Año", "Depreciación", "Dep. Acum", "Valor libros"], tablefmt="fancy_grid"))


