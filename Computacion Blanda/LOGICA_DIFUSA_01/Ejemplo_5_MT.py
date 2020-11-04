import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as sk

# Se define un array x para el manejo del factor de calidad en un restaurante
x = np.arange(0, 11, 1)

# Se define un array para la funcion miembro de tipo triangular
calidad = sk.trimf(x, [10,10,10])

# Se grafica la funcion membresia
plt.figure()
plt.plot(x, calidad, "b", linewidth=1.5, label="Servicio")

plt.title("Calidad del servicio de un restaurante")
plt.ylabel("Membresia")
plt.xlabel("Nivel de servicio")
plt.legend(loc="center right", bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)