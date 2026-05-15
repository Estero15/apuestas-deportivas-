# Importamos librería
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Mi App",
    page_icon="🚀",
    layout="centered"
)

# Contenido
st.title("✨ Mi Primera App en Streamlit")
st.success("✅ Funcionando correctamente!")

# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.write(f"Hola {nombre}, bienvenido a tu proyecto 🎉")

# Gráfico de prueba
datos = pd.DataFrame({
    'Mes': ["Ene", "Feb", "Mar", "Abr", "May"],
    'Ventas': [120, 190, 150, 220, 170]
})

st.subheader("📊 Gráfico de Ventas")
st.line_chart(datos)