import streamlit as st
import pandas as pd
import plotly.express as px


# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Mostrar los primeros datos del DataFrame
st.write(df.head())

import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Cuadro de Mandos - Análisis de Vehículos Usados en Estados Unidos")

# Mostrar los primeros datos del DataFrame
st.write(df.head())

# Crear casilla de verificación para construir un histograma
build_histogram = st.checkbox('Mostrar histograma de precios')

if build_histogram:
    # Crear el histograma con Plotly Express
    fig = px.histogram(df, x='price', nbins=30, title='Distribución de Precios de Vehículos Usados')
    
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig)

# Crear casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión (Precio vs Kilometraje)')

if build_scatter:
    # Crear el gráfico de dispersión con Plotly Express
    fig = px.scatter(df, x='odometer', y='price', title='Relación entre Precio y Kilometraje')
    
    # Mostrar el gráfico en la aplicación
    st.plotly_chart(fig)
    
    
