import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv') 

# 2. Encabezado de la aplicación
st.header('Cuadro de Mandos del Mercado de Vehículos')
st.write('Usa las opciones de abajo para visualizar los análisis de los datos.')

# --- DESAFÍO: CASILLAS DE VERIFICACIÓN ---

# 3. Crear casillas de verificación (devuelven True si están marcadas, False si no)
build_histogram = st.checkbox('Mostrar Histograma')
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión')

# Lógica para el Histograma
if build_histogram:
    st.write('Visualizando la distribución del kilometraje (Odometer):')
    
    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del kilometraje")
    
    # Mostrar el gráfico
    st.plotly_chart(fig_hist, use_container_width=True)

# Lógica para el Gráfico de Dispersión
if build_scatter:
    st.write('Visualizando la relación entre Kilometraje y Precio:')
    
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    
    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
    