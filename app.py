import streamlit as st
import pandas as pd
import plotly.express as px

cars = pd.read_csv("vehicles_us.csv") #Lectura de dataframe

st.title('Programa para crear graficas acerca de ventas de automoviles') # Titulo de la app


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    
    st.header("Presiona el boton para crear un histograma") #indicacion para boton
    hist_button = st.button('Construir histograma') # crear un botón
        
    if hist_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
        # crear un histograma
        fig = px.histogram(cars, x="odometer")
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)



st.header("Presiona el boton para crear un grafico de dispersion") #indicacion para boton

disp_button = st.button('Construir grafico de dispersion') # crear un botón
        
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
    fig = px.scatter(cars, x="odometer", y="price", 
                 title="Gráfico de Dispersión: Odómetro vs Precio",
                 labels={"odometer": "Kilometraje (Odometro)", "price": "Precio (USD)"})
    st.plotly_chart(fig, use_container_width=True)