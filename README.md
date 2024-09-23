MY Test Project
# Análisis de Vehículos Usados en Estados Unidos

Esta aplicación web proporciona un análisis interactivo de un conjunto de datos de anuncios de vehículos usados en Estados Unidos. Utiliza Streamlit como framework para crear la interfaz, pandas para la manipulación de datos y Plotly Express para las visualizaciones interactivas.

## Funcionalidades

- **Visualización de un histograma** que muestra la distribución de los precios de los vehículos usados.
- **Gráfico de dispersión** que muestra la relación entre el precio y el kilometraje (odómetro) de los vehículos.
- Los usuarios pueden seleccionar qué gráficos visualizar mediante **casillas de verificación** interactivas.

## Requisitos

- pandas
- plotly_express
- streamlit

## Instrucciones

Para ejecutar esta aplicación, asegúrate de tener un entorno virtual configurado. Luego, ejecuta el siguiente comando:

```bash
streamlit run app.py



### 3. Archivo `config.toml` para Render

Para que la aplicación funcione en Render, agrega un archivo de configuración `config.toml` en el directorio `streamlit/`. El archivo debe tener el siguiente contenido:

```toml
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000

