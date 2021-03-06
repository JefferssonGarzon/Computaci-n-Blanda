import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as sk

# Se define la variable independiente
x = np.arange(-11, 11, 1)

# Se define la variable dependiente sigmoide de membresia
vd_sigmoide = sk.sigmf(x, 0, 1)

# Se grafica la funcion membresia
plt.figure()
plt.plot(x, vd_sigmoide, "b", linewidth=1.5, label="Servicio")

plt.title("Calidad del servicio de un restaurante")
plt.ylabel("Membresia")
plt.xlabel("Nivel de servicio")
plt.legend(loc="center right", bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)