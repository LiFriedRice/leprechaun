import streamlit as st
import pandas as pd
import plotly.express as px

def generate_plots(df, start_row, end_row):
    if start_row < 0 or end_row >= len(df) or start_row > end_row:
        st.error("Rango de filas no válido. Asegúrate de que el rango sea válido.")
        return None, None, None, None

    df_filtered = df.iloc[start_row:end_row + 1]

    try:
        fig1 = px.bar(df_filtered, x='Year_of_Release', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                      title='Ventas por Año (Gráfico de Barras)')
        fig1.update_layout(barmode='group')

        fig2 = px.line(df_filtered, x='Year_of_Release', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                       title='Ventas por Año (Gráfico de Líneas)')

        fig3 = px.bar(df_filtered, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                      title='Ventas por Género (Gráfico de Barras)')

        fig4 = px.line(df_filtered, x='Genre', y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'],
                       title='Ventas por Género (Gráfico de Líneas)')

        return fig1, fig2, fig3, fig4

    except Exception as e:
        st.error(f"Error al generar gráficos: {e}")
        return None, None, None, None

def main():
    st.title("Data Analysis App")

    uploaded_file = st.file_uploader("Seleccione un archivo CSV", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Archivo cargado exitosamente")

            start_row = st.number_input("Fila de inicio (0-indexado):", min_value=0, value=0)
            end_row = st.number_input("Fila de fin (0-indexado):", min_value=0, value=len(df) - 1)

            fig1, fig2, fig3, fig4 = generate_plots(df, start_row, end_row)
            
            if fig1:
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)
                st.plotly_chart(fig3)
                st.plotly_chart(fig4)

        except Exception as e:
            st.error(f"Error al procesar el archivo CSV: {e}")
    else:
        st.info("Por favor, suba un archivo CSV.")

if __name__ == "__main__":
    main()
