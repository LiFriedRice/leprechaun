import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def generate_plots(df, start_row, end_row):
    df_filtered = df.iloc[start_row:end_row + 1]

    # Años y géneros únicos
    x_years = df_filtered['Year_of_Release'].unique()
    x_Genre = df_filtered['Genre'].unique()

    # Ordenar años y géneros
    x_years = np.sort(x_years)
    x_Genre = np.sort(x_Genre)

    # Convertir años y géneros en índices numéricos
    x_years_indices = np.arange(len(x_years))
    x_Genre_indices = np.arange(len(x_Genre))

    # Crear gráficos
    fig, axs = plt.subplots(2, 2, figsize=(14, 14))
    fig.tight_layout(pad=5.0)

    # Gráfico de barras por año
    df_sorted_years = df_filtered.groupby('Year_of_Release').sum().reindex(x_years).fillna(0)
    bar_width = 0.2
    axs[0, 0].bar(x_years_indices - 1.5 * bar_width, df_sorted_years['NA_Sales'], width=bar_width, label='NA Sales')
    axs[0, 0].bar(x_years_indices - 0.5 * bar_width, df_sorted_years['EU_Sales'], width=bar_width, label='EU Sales')
    axs[0, 0].bar(x_years_indices + 0.5 * bar_width, df_sorted_years['JP_Sales'], width=bar_width, label='JP Sales')
    axs[0, 0].bar(x_years_indices + 1.5 * bar_width, df_sorted_years['Other_Sales'], width=bar_width, label='Other Sales')
    axs[0, 0].set_title('Ventas por Año (Gráfico de Barras)')
    axs[0, 0].set_xlabel('Año')
    axs[0, 0].set_ylabel('Ventas')
    axs[0, 0].set_xticks(x_years_indices)
    axs[0, 0].set_xticklabels(x_years, rotation=90)
    axs[0, 0].legend()

    # Gráfico de líneas por año
    axs[0, 1].plot(x_years_indices, df_sorted_years['NA_Sales'], label='NA Sales', marker='o')
    axs[0, 1].plot(x_years_indices, df_sorted_years['EU_Sales'], label='EU Sales', marker='o')
    axs[0, 1].plot(x_years_indices, df_sorted_years['JP_Sales'], label='JP Sales', marker='o')
    axs[0, 1].plot(x_years_indices, df_sorted_years['Other_Sales'], label='Other Sales', marker='o')
    axs[0, 1].set_title('Ventas por Año (Gráfico de Líneas)')
    axs[0, 1].set_xlabel('Año')
    axs[0, 1].set_ylabel('Ventas')
    axs[0, 1].set_xticks(x_years_indices)
    axs[0, 1].set_xticklabels(x_years, rotation=90)
    axs[0, 1].legend()

    # Gráfico de barras por género
    df_sorted_genre = df_filtered.groupby('Genre').sum().reindex(x_Genre).fillna(0)
    axs[1, 0].bar(x_Genre_indices - 1.5 * bar_width, df_sorted_genre['NA_Sales'], width=bar_width, label='NA Sales')
    axs[1, 0].bar(x_Genre_indices - 0.5 * bar_width, df_sorted_genre['EU_Sales'], width=bar_width, label='EU Sales')
    axs[1, 0].bar(x_Genre_indices + 0.5 * bar_width, df_sorted_genre['JP_Sales'], width=bar_width, label='JP Sales')
    axs[1, 0].bar(x_Genre_indices + 1.5 * bar_width, df_sorted_genre['Other_Sales'], width=bar_width, label='Other Sales')
    axs[1, 0].set_title('Ventas por Género (Gráfico de Barras)')
    axs[1, 0].set_xlabel('Género')
    axs[1, 0].set_ylabel('Ventas')
    axs[1, 0].set_xticks(x_Genre_indices)
    axs[1, 0].set_xticklabels(x_Genre, rotation=90)
    axs[1, 0].legend()

    # Gráfico de líneas por género
    axs[1, 1].plot(x_Genre_indices, df_sorted_genre['NA_Sales'], label='NA Sales', marker='o')
    axs[1, 1].plot(x_Genre_indices, df_sorted_genre['EU_Sales'], label='EU Sales', marker='o')
    axs[1, 1].plot(x_Genre_indices, df_sorted_genre['JP_Sales'], label='JP Sales', marker='o')
    axs[1, 1].plot(x_Genre_indices, df_sorted_genre['Other_Sales'], label='Other Sales', marker='o')
    axs[1, 1].set_title('Ventas por Género (Gráfico de Líneas)')
    axs[1, 1].set_xlabel('Género')
    axs[1, 1].set_ylabel('Ventas')
    axs[1, 1].set_xticks(x_Genre_indices)
    axs[1, 1].set_xticklabels(x_Genre, rotation=90)
    axs[1, 1].legend()

    st.pyplot(fig)

def main():
    st.title("Data Analysis App")
    
    uploaded_file = st.file_uploader("Seleccione un archivo CSV", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Mostrar una vista previa del DataFrame
        st.write("Vista previa del archivo CSV:")
        st.dataframe(df.head())
        
        start_row = st.number_input("Fila de inicio (0-indexado):", min_value=0, value=0)
        end_row = st.number_input("Fila de fin (0-indexado):", min_value=start_row, value=len(df) - 1)
        
        if st.button("Procesar Datos"):
            generate_plots(df, start_row, end_row)

if __name__ == "__main__":
    main()
