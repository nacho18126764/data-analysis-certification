import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importar los datos y establecer la columna 'date' como índice, parseándola como fecha.
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Limpiar los datos filtrando los días en los que las vistas están en el 2,5% inferior o superior.
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]


def draw_line_plot():
    """
    Dibuja un gráfico de línea de las vistas de página diarias.
    Título: Daily freeCodeCamp Forum Page Views 5/2016-12/2019
    Eje x: Date
    Eje y: Page Views
    """
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.tight_layout()
    return fig


def draw_bar_plot():
    """
    Dibuja un gráfico de barras que muestra el promedio de vistas diarias para cada mes, agrupado por año.
    Eje x: Years
    Eje y: Average Page Views
    Leyenda: Months (con etiquetas de meses)
    """
    # Crear una copia para el gráfico de barras
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    # Convertir el número de mes en nombre abreviado
    month_names = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    df_bar["month"] = df_bar["month"].map(month_names)

    # Agrupar por año y mes y calcular el promedio de vistas
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Asegurar el orden correcto de los meses
    df_bar = df_bar[["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

    fig, ax = plt.subplots(figsize=(10, 8))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.tight_layout()
    return fig


def draw_box_plot():
    """
    Dibuja dos diagramas de caja adyacentes:
      - Diagrama de caja por año: muestra la distribución anual de las vistas.
      - Diagrama de caja por mes: muestra la distribución por mes (con orden correcto, iniciando en Jan).
    """
    # Copia de los datos y reiniciar el índice para tener 'date' como columna.
    df_box = df.copy().reset_index()
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.month

    # Mapear el número del mes a su nombre abreviado
    month_names = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
        7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }
    df_box["month"] = df_box["month"].map(month_names)

    # Crear la figura con dos subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    # Diagrama de caja por año (Tendencia)
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Diagrama de caja por mes (Estacionalidad) con el orden correcto
    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x="month", y="value", data=df_box, order=order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    return fig
