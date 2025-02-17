import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Cargar los datos desde el archivo CSV
df = pd.read_csv('medical_examination.csv')

# 2. Agregar la columna 'overweight' calculando el IMC
df['height'] = df['height'] / 100  # Convertir altura a metros
df['bmi'] = df['weight'] / (df['height'] ** 2)  # Calcular IMC
df['overweight'] = (df['bmi'] > 25).astype(int)  # Sobrepeso si IMC > 25

# 3. Normalizar los datos: si colesterol o gluc es 1, asignar 0; si es >1, asignar 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Crear la función para la gráfica categórica
def draw_cat_plot():
    # Crear un DataFrame en formato largo para el gráfico
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Renombrar la columna 'variable' a 'feature' para mejor claridad
    df_cat = df_cat.rename(columns={"variable": "feature", "value": "value"})

    # Crear la gráfica usando seaborn
    fig = sns.catplot(x="feature", hue="value", col="cardio", data=df_cat, kind="count")

    # Ajustar títulos y etiquetas
    fig.set_axis_labels("Feature", "Count")
    fig.set_titles("Cardio Status: {col_name}")

    # Mostrar la gráfica
    plt.show()

# Llamar la función para dibujar la gráfica
draw_cat_plot()

# 5. Limpiar los datos de acuerdo con las condiciones proporcionadas
def clean_data():
    df_clean = df[
        (df['ap_lo'] <= df['ap_hi']) &  # La presión diastólica no puede ser mayor que la sistólica
        (df['height'] >= df['height'].quantile(0.025)) &  # Altura mayor que el 2.5 percentil
        (df['height'] <= df['height'].quantile(0.975)) &  # Altura menor que el 97.5 percentil
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Peso mayor que el 2.5 percentil
        (df['weight'] <= df['weight'].quantile(0.975))  # Peso menor que el 97.5 percentil
    ]
    return df_clean

# Limpiar los datos
df_clean = clean_data()

# 6. Crear la función para la gráfica del mapa de calor (Heat Map)
def draw_heat_map():
    # Calcular la matriz de correlación
    corr = df_clean.corr()

    # Crear la máscara para el triángulo superior de la matriz
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Configurar la figura de matplotlib
    plt.figure(figsize=(10, 8))

    # Dibujar el mapa de calor
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={'shrink': 0.8})

    # Mostrar el gráfico
    plt.show()

# Llamar la función para dibujar el mapa de calor
draw_heat_map()
