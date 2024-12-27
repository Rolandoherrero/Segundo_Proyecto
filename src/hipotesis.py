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
        x='Temperature',
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
    mfd['rango_temperatura'] = pd.cut(mfd['Temperature'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Failure_Risk'] == 1].groupby('rango_temperatura')['Failure_Risk'].count()

    # Crear el gráfico de barras
    fig_2, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de Temperatura', fontsize=25, color='white')
    ax.set_xlabel('Rango de Temperatura', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  # Rotar a horizontal y ajustar distancia
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    #Tabla de porcentajes
    data1 = {
    "Categoría": ["Temperatura baja", "Temperatura media", "Temperatura alta"],
    "Porcentaje (%)": [25.85, 30.64, 33.33] 
    }

    df1 = pd.DataFrame(data1)

    return fig_1, fig_2, df1


 #Hipotesis 2
def hipotesis_2(mfd):
        #Grafico 1: histograma de la vibración
    fig_4 = px.histogram(
        data_frame=mfd,
        x='Vibration',
        title = "Histograma de la vibración",
        )

    fig_4.update_layout(
        title=dict(
            text="Histograma de la vibración",
            font=dict(size=25, family="Arial", color="white"),
            x=0.30  
        ),
        xaxis_title=dict(
            text="Vibración",
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

        #Grafico 2: Grafico de barras por rango de vibración
    bins = [35, 45, 55, 66]
    labels = ['35-45', '45-55', '55-66']
    mfd['rango_vibración'] = pd.cut(mfd['Vibration'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Failure_Risk'] == 1].groupby('rango_vibración')['Failure_Risk'].count()

    # Crear el gráfico de barras
    fig_5, ax = plt.subplots(figsize=(8, 6))
    ax.bar(fallas_por_rango.index, fallas_por_rango.values, color=['blue', 'orange', 'red'])
    ax.set_title('Riesgo de Falla por Rango de Vibración', fontsize=25, color='white')
    ax.set_xlabel('Rango de vibración', fontsize=20, color='white')
    ax.set_ylabel('Riesgo de Fallas', fontsize=20, color='white', rotation=0, labelpad=50)  # Rotar a horizontal y ajustar distancia
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)   

    #Tabla de porcentajes
    data2 = {
        "Categoría": ["Vibración baja", "Vibración media", "Vibración alta"],
        "Porcentaje (%)": [31.65, 29.05, 32.39] 
    }

    df2 = pd.DataFrame(data2)


    return fig_4, fig_5, df2

 #Hipotesis 3
def hipotesis_3(mfd):
        #Grafico 1: histograma de la potencia
    fig_7 = px.histogram(
        data_frame=mfd,
        x='Power_Usage',
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
    mfd['rango_potencia'] = pd.cut(mfd['Power_Usage'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Failure_Risk'] == 1].groupby('rango_potencia')['Failure_Risk'].count()

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
        "Categoría": ["Baja potencia", "Media potencia", "Alta potencia"],
        "Porcentaje (%)": [25.66, 30.71, 31.31] 
    }

    df3 = pd.DataFrame(data3)

    return fig_7, fig_8, df3

 #Hipotesis 4
def hipotesis_4(mfd):
        #Grafico 1: histograma de la humedad
    fig_10 = px.histogram(
        data_frame=mfd,
        x='Humidity',
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
    mfd['rango_humedad'] = pd.cut(mfd['Humidity'], bins=bins, labels=labels, right=False)

    # Contar fallas en cada rango
    fallas_por_rango = mfd[mfd['Failure_Risk'] == 1].groupby('rango_humedad')['Humidity'].count()

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
    "Categoría": ["Humedad baja", "Humedad media", "Humedad alta"],
    "Porcentaje (%)": [33.65, 29.32, 27.10] 
    }

    df4 = pd.DataFrame(data4)

    return fig_10, fig_11, df4

 #Hipotesis 5
def hipotesis_5(mfd):
        #Grafico 2: Grafico de barras por tipo de máquina
    labels = ['Perforadora', 'Torno', 'Molino']
    fallas_por_tipo = mfd.groupby("Machine_Type")["Failure_Risk"].sum()

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