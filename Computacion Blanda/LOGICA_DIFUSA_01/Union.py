import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt 

#defincion de arreglo para calidad
x = np.arange(0, 11, 1)

#definiendo funciones triangulares
bajo = sk.trimf(x,[0,0,5])
medio = sk.trimf(x,[0,5,10])

#graficacion
plt.figure()
plt.plot(x, bajo, "b", linewidth = 1.5, label="Bajo")
plt.plot(x, medio, "r", linewidth = 1.5, label="Medio")

#ajustes gráfico
plt.title("Funcion Union (máximo")
plt.ylabel("Membresia")
plt.xlabel("Velocidad (Kilometros por hora)")
plt.legend(loc="center right", bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)

i = 0
while i<=10: 
    plt.axvline(x=0, ymin=0, ymax=10, color="g", linestyle="-.")
    i+=1

plt.plot(0, 1, marker="o", markersize=10, color="g")
plt.plot(1, 0.8, marker="o", markersize=10, color="g")
plt.plot(2, 0.6, marker="o", markersize=10, color="g")
plt.plot(3, 0.6, marker="o", markersize=10, color="g")
plt.plot(4, 0.8, marker="o", markersize=10, color="g")
plt.plot(5, 1, marker="o", markersize=10, color="g")

plt.plot(6, 0.8, marker="o", markersize=10, color="g")
plt.plot(7, 0.6, marker="o", markersize=10, color="g")
plt.plot(8, 0.4, marker="o", markersize=10, color="g")
plt.plot(9, 0.2, marker="o", markersize=10, color="g")
plt.plot(10, 0, marker="o", markersize=10, color="g")

plt.show()

# encontrando el maximo (Fuzzy OR)
sk.fuzzy_or(x, bajo, x, medio)
