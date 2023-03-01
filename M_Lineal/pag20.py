from tabulate import tabulate
import csv, datetime
import matplotlib.pyplot as plt
import numpy as np
from progress.bar import Bar, ChargingBar, FillingCirclesBar, FillingSquaresBar, IncrementalBar, PixelBar, ShadyBar
import os, time, random
C = float(input("Ingrese el costo del activo: "))
B = float(input("Ingrese el valor de la base: "))
#solicitar valores de uso de activo en forma de lista de floats
nt = [float(x) for x in input("Ingrese los valores de uso del activo en forma de lista separados por comas: ").split(",")]

ntV = sum(nt)
n = len(nt)
ntA = [0]
dep = [0]
depA = [0]
vt = [0]
vt[0] = C
for i in range(1,n):
    ntA.append(ntA[i-1] + nt[i])
    dep.append((B/ntV)*nt[i])
    depA.append(depA[i-1] + dep[i])
    vt.append(C - depA[i])    

table = []
for i in range(n):
    table.append([i,nt[i],ntA[i],round(dep[i],2),round(depA[i],2),round(vt[i],2)])


#generar menu de opciones para consultar datos de la tabla
os.system("cls")
while True:
    print("Variables definidas:")
    print("C = ",C)
    print("B = ",B)
    print("1. Consultar valor de un año")
    print("2. Consultar valor de varios años")
    print("3. Generar tabla")
    print("4. Generar gráfico")
    print("5. Guardar tabla (CSV)")
    print("6. Limpiar pantalla")
    print("7. Salir")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        os.system("cls")
        #mostrar barra de progreso para el usuario
        #consultar valor de un año
        a = int(input("Ingrese el año a consultar: "))
        bar2 = IncrementalBar('Procesando', max = 100)
        for i in range(100):
            time.sleep(0.001)
            bar2.next()
        bar2.finish()
        #mostrar renglon de la tabla
        print(tabulate([table[a]], headers=["Año", "Uso", "Acumulado", "Depreciación", "Dep. Acum", "Valor libros"], tablefmt="fancy_grid"))
    elif op == 2:
        os.system("cls")
        #consultar valor de varios años
        a1 = int(input("Ingrese el año inicial: "))
        a2 = int(input("Ingrese el año final: "))
        #mostrar barra de progreso para el usuario
        bar3 = IncrementalBar('Procesando', max = 100)
        for i in range(100):
            time.sleep(0.001)
            bar3.next()
        bar3.finish()
        #mostrar renglones de la tabla
        print(tabulate(table[a1:a2+1], headers=["Año", "Uso", "Acumulado", "Depreciación", "Dep. Acum", "Valor libros"], tablefmt="fancy_grid"))
    elif op == 3:
        os.system("cls")
        #generar grafico
        #mostrar barra de progreso para el usuario
        bar5 = IncrementalBar('Generando gráfico', max = 100)
        for i in range(100):
            time.sleep(0.001)
            bar5.next()
        bar5.finish()

        print(tabulate(table, headers=["Año", "Uso", "Acumulado", "Depreciación", "Dep. Acum", "Valor libros"], tablefmt="fancy_grid"))
    elif op == 4:
        os.system("cls")
        #generar grafico
        #mostrar barra de progreso para el usuario
        bar5 = IncrementalBar('Generando gráfico', max = 100)
        for i in range(100):
            time.sleep(0.001)
            bar5.next()
        bar5.finish()
        #generar grafico
        plt.plot([i for i in range(n)],vt)
        #agregar etiquetas
        plt.xlabel("Años")
        plt.ylabel("Valor de libros")
        plt.title("Gráfico de depreciación del activo")
        plt.show()
    elif op == 5:
        os.system("cls")
        #guardar tabla en archivo csv
        #mostrar barra de progreso para el usuario
        bar4 = IncrementalBar('Guardando archivo', max = 100)
        for i in range(100):
            time.sleep(0.001)
            bar4.next()
        bar4.finish()
        # Guardar tabla en archivo CSV
        now = datetime.date.today()
        filename = f"matematicas_{now.strftime('%Y%m%d')}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Año', 'Uso', 'Acumulado', 'Depreciación', 'Dep. Acum', 'Valor libros'])
            for row in table:
                writer.writerow(row)
        print("Archivo guardado")
    elif op == 6:
        #limpiar pantalla
        os.system("cls")
    elif op == 7:
        os.system("cls")
        #mostrar barra de progreso para el usuario
        print("Saliendo...")
        print("Gracias por usar el programa")
        #salir
        break
    else:
        #opcion invalida
        print("Opción inválida")
