import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib as plt
from src.hipotesis import hipotesis_1, hipotesis_2, hipotesis_3, hipotesis_4, hipotesis_5

#Cargar el dataframe
@st.cache_data
def load_data():
    return pd.read_csv("data/machine_failure_dataset.csv")

#Cargar datos
mfd = load_data()

st.title("Hipotesis del Proyecto")

#Hipotesis 1
st.header("Hipotesis 1: A medida que la temperatura operativa de la máquina incrementa, aumenta el riesgo de fallo")
fig_1, fig_2, df1 = hipotesis_1(mfd)
st.plotly_chart(fig_1, use_container_width=True)
st.plotly_chart(fig_2, use_container_width=True)
st.subheader("Tabla de Porcentajes de Falla por Rango de Temperatura")
st.table(df1)

#Hipotesis 2
st.header("Hipotesis 2:  Un mayor nivel de vibración en la máquina incrementa la probabilidad de fallo.")
fig_4, fig_5, df2 = hipotesis_2(mfd)
st.plotly_chart(fig_4, use_container_width=True)
st.plotly_chart(fig_5, use_container_width=True)
st.subheader("Tabla de Porcentajes de Falla por Rango de Vibración")
st.table(df2)

#Hipotesis 3
st.header("Hipotesis 3:  Una menor potencia de operación se asocia con una reducción en la probabilidad de fallo de la máquina.")
fig_7, fig_8, df3 = hipotesis_3(mfd)
st.plotly_chart(fig_7, use_container_width=True)
st.plotly_chart(fig_8, use_container_width=True)
st.subheader("Tabla de Porcentajes de Falla por Rango de Potencia Empleada")
st.table(df3)

#Hipotesis 4
st.header("Hipotesis 4:  La acumulación de humedad en la máquina incrementa la probabilidad de fallo.")
fig_10, fig_11, df4 = hipotesis_4(mfd)
st.plotly_chart(fig_10, use_container_width=True)
st.plotly_chart(fig_11, use_container_width=True)
st.subheader("Tabla de Porcentajes de Falla por Rango de Humedad")
st.table(df4)

#Hipotesis 5
st.header("Hipotesis 5:  Las máquinas perforadoras presentan un mayor riesgo de fallo en comparación con otros tipos de máquinas.")
fig_13, df5 = hipotesis_5(mfd)
st.plotly_chart(fig_13, use_container_width=True)
st.subheader("Tabla de Porcentajes de Falla por Tipo de Máquina")
st.table(df5)
