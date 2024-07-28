import streamlit as st

# Título de la aplicación
st.title('Mostrar Código desde Repositorio Local')

# Especifica el archivo que quieres mostrar
archivo_codigo = 'carga_datos'  # Reemplaza con la ruta correcta

# Lee el contenido del archivo
try:
    with open(archivo_codigo, 'r') as file:
        codigo = file.read()
except FileNotFoundError:
    st.error(f"Archivo {archivo_codigo} no encontrado.")
    codigo = ""

# Muestra el código con resaltado de sintaxis
st.code(codigo, language='python')
