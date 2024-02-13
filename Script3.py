import matplotlib.pyplot as plt
import numpy as np

# Definimos los rangos de valores para x
x = np.linspace(-10, 10, 400)

# Definimos la función y = x^2
y = x**2

# Creamos la gráfica
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = x^2')

plt.title('Gráfica de la Función y = x^2')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
