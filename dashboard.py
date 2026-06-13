import streamlit as st
import requests
import pandas as pd

st.title("📊 Dashboard de Usuarios")

# Consumir API
respuesta = requests.get(
    "http://127.0.0.1:8000/usuarios"
)

usuarios = respuesta.json()

# Convertir a DataFrame
df = pd.DataFrame(usuarios)

# Mostrar tabla
st.subheader("Usuarios")

st.dataframe(df)

st.subheader("📈 Estadísticas")

st.metric(
    "Total usuarios",
    len(df)
)

st.metric(
    "Edad promedio",
    round(df["edad"].mean(), 2)
)

st.metric(
    "Edad máxima",
    df["edad"].max()
)

st.metric(
    "Edad mínima",
    df["edad"].min()
)

st.subheader("📊 Distribución de edades")

st.bar_chart(df["edad"])