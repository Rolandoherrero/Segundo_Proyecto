import streamlit as st 
import pandas as pd
import seaborn as sns
from src.eda import bargraphic, cajasbigotes, graficodispersion

#Carga el dataframe
@st.cache_data
def load_data():
    return pd.read_csv('data/machine_failure_dataset.csv')

#Configuracion de la pagina
st.title("Análisis Exploratotio de Datos (EDA)")

#Cargar datos
mfd=load_data()

#Informacion basica del conjunto de datos 
st.header("Aspectos Básicos del Conjunto de Datos")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1: 
        st.metric(label="Número de filas", value=mfd.shape[0], border=True)
        with col2:
            st.metric(label="Número de columans", value=mfd.shape[1], border=True)
            with col3:
                missing_values=mfd.isnull().any().sum()
                st.metric(label="Valores perdidos", value="Si" if missing_values > 0 else "No", border = True)

#Mostrar graficos
st.header("Gráfico de barras de cantidad de máquinas por tipo")
bargraphic_fig = bargraphic(mfd)
st.plotly_chart(bargraphic_fig)

st.header("Distribución de temperatura segun el tipo de máquina")
cajasbigotes_fig = cajasbigotes(mfd)
st.plotly_chart(cajasbigotes_fig)

st.header("Relación entre la vibración y la potencia usada")
graficodispersion_fig = graficodispersion(mfd)
st.plotly_chart(graficodispersion_fig)

