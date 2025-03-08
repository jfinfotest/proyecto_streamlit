import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("Mi primera aplicación con Streamlit")

# Texto simple
st.write("¡Hola! Esta es una aplicación básica.")

# Agregar un campo de entrada
nombre = st.text_input("Ingresa tu nombre:")

# Mostrar un mensaje personalizado
if nombre:
    st.write(f"Hola, {nombre}, ¿cómo estás?")
    
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


datos = ("Email", "Home phone", "Mobile phone")

import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    datos,
)

st.write("You selected:", option)