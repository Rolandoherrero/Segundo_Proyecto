#hip.py
import matplotlib as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#Hipotesis 1
def hipotesis_1(mfd):

        #Grafico 1: histograma de la temperatura
    fig_1 = px.histogram(
        data_frame=mfd,
        x='Temperatura',
        title = "Histograma de la temperatura",
        )

    fig_1.update_layout(
        title=dict(
            text="Histograma de la temperatura",
            font=dict(size=25, family="Arial", color="white"),
            x=0.30  # Centrar el título
        ),
        xaxis_title=dict(
            text="Temperatura",
            font=dict(size=19, family="Arial", color="white")
        ),
        yaxis_title=None,  # Desactivar el título por defecto del eje Y
    )

    fig_1.add_annotation(
        xref="paper",
        yref="paper",
        x=0,  
        y=1.05, 
        text="Frecuencia",
        showarrow=False,
        font=dict(size=19, family="Arial", color="white"),
        textangle=0,  
        xanchor="left",
        yanchor="bottom"
    )

        #Grafico 2: Grafico de barras por rango de temperatura
    bins = [36, 60, 90, 110]
    labels = ['36-60', '60-90', '90-110']
    mfd['rango_temperatura'] = pd.cut(mfd['Temperatura'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Riesgo_de_Falla'] == 1].groupby('rango_temperatura')['Riesgo_de_Falla'].count()

    # Crear el gráfico de barras
    fig_2, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de Temperatura', fontsize=25, color='white')
    ax.set_xlabel('Rango de Temperatura', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50) 
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    #Tabla de porcentajes
    data1 = {
    "Categoría": ["Temperatura baja (36-60)", "Temperatura media(60-90)", "Temperatura alta(90-110)"],
    "Porcentaje (%)": [25.85, 30.64, 33.33] 
    }

    df1 = pd.DataFrame(data1)

    return fig_1, fig_2, df1


 #Hipotesis 2
def hipotesis_2(mfd):
        #Grafico 1: histograma de la Vibracion
    fig_4 = px.histogram(
        data_frame=mfd,
        x='Vibracion',
        title = "Histograma de la Vibracion",
        )

    fig_4.update_layout(
        title=dict(
            text="Histograma de la Vibracion",
            font=dict(size=25, family="Arial", color="white"),
            x=0.30  
        ),
        xaxis_title=dict(
            text="Vibracion",
            font=dict(size=19, family="Arial", color="white")
        ),
        yaxis_title=None,  
    )

    fig_4.add_annotation(
        xref="paper",
        yref="paper",
        x=0,  
        y=1.05, 
        text="Frecuencia",
        showarrow=False,
        font=dict(size=19, family="Arial", color="white"),
        textangle=0,  
        xanchor="left",
        yanchor="bottom"
    )

        #Grafico 2: Grafico de barras por rango de Vibracion
    bins = [35, 45, 55, 66]
    labels = ['35-45', '45-55', '55-66']
    mfd['rango_Vibracion'] = pd.cut(mfd['Vibracion'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Riesgo_de_Falla'] == 1].groupby('rango_Vibracion')['Riesgo_de_Falla'].count()

    # Crear el gráfico de barras
    fig_5, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de Vibracion', fontsize=25, color='white')
    ax.set_xlabel('Rango de Vibracion', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  # Rotar a horizontal y ajustar distancia
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)   

    #Tabla de porcentajes
    data2 = {
        "Categoría": ["Vibracion baja(35-45)", "Vibracion media(45-55)", "Vibracion alta(55-66)"],
        "Porcentaje (%)": [31.65, 29.05, 32.39] 
    }

    df2 = pd.DataFrame(data2)


    return fig_4, fig_5, df2

 #Hipotesis 3
def hipotesis_3(mfd):
        #Grafico 1: histograma de la potencia
    fig_7 = px.histogram(
        data_frame=mfd,
        x='Potencia_Empleada',
        title = "Histograma de la potencia",
        )

    fig_7.update_layout(
        title=dict(
            text="Histograma de la potencia",
            font=dict(size=25, family="Arial", color="white"),
            x=0.30  
        ),
        xaxis_title=dict(
            text="Potencia",
            font=dict(size=19, family="Arial", color="white")
        ),
        yaxis_title=None,  
    )

    fig_7.add_annotation(
        xref="paper",
        yref="paper",
        x=0,  
        y=1.05, 
        text="Frecuencia",
        showarrow=False,
        font=dict(size=19, family="Arial", color="white"),
        textangle=0,  
        xanchor="left",
        yanchor="bottom"
    )

        #Grafico 2: Grafico de barras por rango de Potencia
    bins = [3.5, 8, 12.5, 18]
    labels = ['3.5-8', '8-12.5', '12.5-18']
    mfd['rango_potencia'] = pd.cut(mfd['Potencia_Empleada'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Riesgo_de_Falla'] == 1].groupby('rango_potencia')['Riesgo_de_Falla'].count()

    # Crear el gráfico de barras
    fig_8, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de potencia', fontsize=25, color='white')
    ax.set_xlabel('Rango de potencia', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  # Rotar a horizontal y ajustar distancia
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7) 

    #Tabla de porcentajes
    data3 = {
        "Categoría": ["Baja potencia(3.5-8)", "Media potencia(8-12.5)", "Alta potencia(12.5-18)"],
        "Porcentaje (%)": [25.66, 30.71, 31.31] 
    }

    df3 = pd.DataFrame(data3)

    return fig_7, fig_8, df3

 #Hipotesis 4
def hipotesis_4(mfd):
        #Grafico 1: histograma de la humedad
    fig_10 = px.histogram(
        data_frame=mfd,
        x='Humedad',
        title = "Histograma de la humedad",
        )

    fig_10.update_layout(
        title=dict(
            text="Histograma de la humedad",
            font=dict(size=25, family="Arial", color="white"),
            x=0.30  
        ),
        xaxis_title=dict(
            text="Humedad",
            font=dict(size=19, family="Arial", color="white")
        ),
        yaxis_title=None,  
    )

    fig_10.add_annotation(
        xref="paper",
        yref="paper",
        x=0,  
        y=1.05, 
        text="Frecuencia",
        showarrow=False,
        font=dict(size=19, family="Arial", color="white"),
        textangle=0,  
        xanchor="left",
        yanchor="bottom"
    )

        #Grafico 2: Grafico de barras por rango de Humedad
    bins = [15, 25.66, 36.33, 47]
    labels = ['15-25.66', '25.66-36.33', '36.33-47']
    mfd['rango_humedad'] = pd.cut(mfd['Humedad'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Riesgo_de_Falla'] == 1].groupby('rango_humedad')['Humedad'].count()

    # Crear el gráfico de barras
    fig_11, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de humedad', fontsize=25, color='white')
    ax.set_xlabel('Rango de humedad', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)  

    #Tabla de porcentajes
    data4 = {
    "Categoría": ["Humedad baja(15-25.66)", "Humedad media(25.66-36.33)", "Humedad alta(36.33-47)"],
    "Porcentaje (%)": [33.65, 29.32, 27.10] 
    }

    df4 = pd.DataFrame(data4)

    return fig_10, fig_11, df4

 #Hipotesis 5
def hipotesis_5(mfd):
        #Grafico 2: Grafico de barras por tipo de máquina
    labels = ['Perforadora', 'Torno', 'Molino']
    fallas_por_tipo = mfd.groupby("Tipo_de_Maquina")["Riesgo_de_Falla"].sum()

    # Crear el gráfico de barras
    fig_13, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_tipo.index, fallas_por_tipo.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por tipo de máquina', fontsize=25, color='white')
    ax.set_xlabel('Tipo de máquina', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)  

    #Tabla de porcentajes
    data5 = {
    "Categoría": ["Máquina Perforadora", "Máquina Torno", "Máquina Molino"],
    "Porcentaje (%)": [31.14, 31.06, 27.74],
    }

    df5 = pd.DataFrame(data5)

    return fig_13, df5