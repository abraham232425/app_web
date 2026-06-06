# app_web
Proyecto sprint 7
# Cuadro de Mandos - Análisis del Mercado de Vehículos

Este proyecto es una aplicación web interactiva desarrollada en Python que permite explorar un conjunto de datos sobre anuncios de venta de coches en los Estados Unidos. El objetivo principal es facilitar el Análisis Exploratorio de Datos (EDA) a través de herramientas visuales dinámicas.

## Funcionalidades de la Aplicación
La aplicación web proporciona las siguientes herramientas interactivas:
* **Filtros dinámicos (Casillas de verificación):** Permiten al usuario decidir qué visualizaciones desplegar en tiempo real.
* **Histograma interactivo:** Representa la distribución del kilometraje (`odometer`) de los vehículos publicados.
* **Gráfico de dispersión:** Analiza la relación directa entre el kilometraje de los autos y su precio de venta, segmentado de forma visual.

## Tecnologías Utilizadas
* **Python**
* **Streamlit** (para la creación de la interfaz web)
* **Pandas** (para la manipulación y lectura del dataset)
* **Plotly Express** (para la generación de gráficos interactivos)

## Cómo ejecutar el proyecto localmente
1. Clona este repositorio.
2. Asegúrate de tener instalado tu entorno virtual con las librerías del archivo `requirements.txt`.
3. Ejecuta el comando en tu terminal:
   ```bash
   streamlit run app.py