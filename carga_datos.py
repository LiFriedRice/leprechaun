import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Función para generar gráficos
def generate_plots(df, start_row, end_row):
    df_filtered = df.iloc[start_row:end_row + 1]

    # Gráfico de barras por año
    fig1 = px.bar(df_filtered, x='Year_of_Release', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                  title='Ventas por Año (Gráfico de Barras)')
    fig1.update_layout(barmode='group')

    # Gráfico de líneas por año
    fig2 = px.line(df_filtered, x='Year_of_Release', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                   title='Ventas por Año (Gráfico de Líneas)')

    # Gráfico de barras por género
    fig3 = px.bar(df_filtered, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                  title='Ventas por Género (Gráfico de Barras)')

    # Gráfico de líneas por género
    fig4 = px.line(df_filtered, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                   title='Ventas por Género (Gráfico de Líneas)')

    return fig1, fig2, fig3, fig4

# Interfaz de usuario con Streamlit
def main():
    st.title("Data Analysis App")

    # Subir archivo
    uploaded_file = st.file_uploader("Seleccione un archivo CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Archivo cargado exitosamente")
        
        # Entrada de filas de inicio y fin
        start_row = st.number_input("Fila de inicio (0-indexado):", min_value=0, value=0)
        end_row = st.number_input("Fila de fin (0-indexado):", min_value=0, value=len(df) - 1)

        # Verificar que end_row no sea menor que start_row
        if end_row < start_row:
            st.error("La fila de fin no puede ser menor que la fila de inicio.")
        else:
            # Generar y mostrar gráficos
            fig1, fig2, fig3, fig4 = generate_plots(df, start_row, end_row)
            
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)
            st.plotly_chart(fig4)
    else:
        st.info("Por favor, suba un archivo CSV.")

if __name__ == "__main__":
    main()
