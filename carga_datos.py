import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv('Datos.csv')

# Años y géneros únicos
x_years = df['Year_of_Release'].unique()
x_Genre = df['Genre'].unique()

# Ordenar años y géneros
x_years = np.sort(x_years)
x_Genre = np.sort(x_Genre)

# Convertir años y géneros en índices numéricos
x_years_indices = np.arange(len(x_years))
x_Genre_indices = np.arange(len(x_Genre))

# Para el gráfico de barras por año
plt.figure(figsize=(14,7))  # Establecer el tamaño de la figura
bar_width = 0.2
# Asegurarse de que los datos estén ordenados por año
df_sorted_years = df.groupby('Year_of_Release').sum().reindex(x_years).fillna(0)
plt.bar(x_years_indices - 1.5 * bar_width, df_sorted_years['NA_Sales'], width=bar_width, label='NA Sales')
plt.bar(x_years_indices - 0.5 * bar_width, df_sorted_years['EU_Sales'], width=bar_width, label='EU Sales')
plt.bar(x_years_indices + 0.5 * bar_width, df_sorted_years['JP_Sales'], width=bar_width, label='JP Sales')
plt.bar(x_years_indices + 1.5 * bar_width, df_sorted_years['Other_Sales'], width=bar_width, label='Other Sales')
plt.title('Ventas por Año (Gráfico de Barras)')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.xticks(x_years_indices, x_years)
plt.legend()
plt.tight_layout()
plt.savefig('/var/www/html/leprechaun/Graficos/ventas_por_año_barras.png')
plt.close()

# Para el gráfico de líneas por año
plt.figure(figsize=(14,7))  # Establecer el tamaño de la figura
plt.plot(x_years_indices, df_sorted_years['NA_Sales'], label='NA Sales', marker='o')
plt.plot(x_years_indices, df_sorted_years['EU_Sales'], label='EU Sales', marker='o')
plt.plot(x_years_indices, df_sorted_years['JP_Sales'], label='JP Sales', marker='o')
plt.plot(x_years_indices, df_sorted_years['Other_Sales'], label='Other Sales', marker='o')
plt.title('Ventas por Año (Gráfico de Líneas)')
plt.xlabel('Año')
plt.ylabel('Ventas')
plt.xticks(x_years_indices, x_years)
plt.legend()
plt.tight_layout()
plt.savefig('/var/www/html/leprechaun/Graficos/ventas_por_año_lineas.png')
plt.close()

# Para el gráfico de barras por género
plt.figure(figsize=(14,7))  # Establecer el tamaño de la figura
# Asegurarse de que los datos estén ordenados por género
df_sorted_genre = df.groupby('Genre').sum().reindex(x_Genre).fillna(0)
plt.bar(x_Genre_indices - 1.5 * bar_width, df_sorted_genre['NA_Sales'], width=bar_width, label='NA Sales')
plt.bar(x_Genre_indices - 0.5 * bar_width, df_sorted_genre['EU_Sales'], width=bar_width, label='EU Sales')
plt.bar(x_Genre_indices + 0.5 * bar_width, df_sorted_genre['JP_Sales'], width=bar_width, label='JP Sales')
plt.bar(x_Genre_indices + 1.5 * bar_width, df_sorted_genre['Other_Sales'], width=bar_width, label='Other Sales')
plt.title('Ventas por Plataforma (Gráfico de Barras)')
plt.xlabel('Género')
plt.ylabel('Ventas')
plt.xticks(x_Genre_indices, x_Genre, rotation=90)  # Rotar las etiquetas si son largas
plt.legend()
plt.tight_layout()
plt.savefig('/var/www/html/leprechaun/Graficos/ventas_por_genero_barras.png')
plt.close()

# Para el gráfico de líneas por género
plt.figure(figsize=(14,7))  # Establecer el tamaño de la figura
plt.plot(x_Genre_indices, df_sorted_genre['NA_Sales'], label='NA Sales', marker='o')
plt.plot(x_Genre_indices, df_sorted_genre['EU_Sales'], label='EU Sales', marker='o')
plt.plot(x_Genre_indices, df_sorted_genre['JP_Sales'], label='JP Sales', marker='o')
plt.plot(x_Genre_indices, df_sorted_genre['Other_Sales'], label='Other Sales', marker='o')
plt.title('Ventas por Plataforma (Gráfico de Líneas)')
plt.xlabel('Género')
plt.ylabel('Ventas')
plt.xticks(x_Genre_indices, x_Genre, rotation=90)  # Rotar las etiquetas si son largas
plt.legend()
plt.tight_layout()
plt.savefig('/var/www/html/leprechaun/Graficos/ventas_por_genero_lineas.png')
plt.close()
