import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# 1. Importar los datos
df = pd.read_csv("epa-sea-level.csv")

# 2. Crear el scatter plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", s=10)

# 3. Obtener la línea de mejor encaje para todos los datos
# Se calcula la regresión lineal en el rango de años desde el mínimo hasta 2050
years_full = np.arange(df["Year"].min(), 2051)
slope_full, intercept_full, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
# Calcular los valores predichos usando la recta de regresión
predicted_full = slope_full * years_full + intercept_full
ax.plot(years_full, predicted_full, color="red", label="Fit: All Data")

# 4. Obtener la línea de mejor encaje para datos desde el año 2000 en adelante
df_2000 = df[df["Year"] >= 2000]
years_2000 = np.arange(2000, 2051)
slope_2000, intercept_2000, r_value2, p_value2, std_err2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
predicted_2000 = slope_2000 * years_2000 + intercept_2000
ax.plot(years_2000, predicted_2000, color="green", label="Fit: Data from 2000")

# 5. Etiquetar ejes y título
ax.set_xlabel("Year")
ax.set_ylabel("Sea Level (inches)")
ax.set_title("Rise in Sea Level")
ax.legend()

plt.tight_layout()

# Guardar la figura si es necesario (por ejemplo: fig.savefig('sea_level_plot.png'))
plt.show()

# Si se requiere devolver la figura, se puede incluir:
# return fig
