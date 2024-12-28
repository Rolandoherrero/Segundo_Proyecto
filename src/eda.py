import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

def bargraphic(mfd):
    """Gráfico de barras de la cantidad de máquinas de cada tipo."""
    tipo = mfd["Tipo_de_Maquina"].value_counts()
    fig = go.Figure(
        data=[
            go.Bar(
                x=tipo.index,
                y=tipo.values,
                marker=dict(color=['skyblue', 'orange', 'green'])
            )
        ]
    )
    fig.update_layout(
        title='Cantidad de Máquinas por Tipo',
        xaxis_title='Tipo de Máquina',
        yaxis_title='Cantidad',
        xaxis=dict(tickangle=0),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
    )
    return fig


def cajasbigotes(mfd):
    """Gráfico de cajas y bigotes para temperatura según el tipo de máquina."""
    fig = px.box(
        mfd,
        x='Tipo_de_Maquina',
        y='Temperatura',
        title='Distribución de temperatura según el tipo de máquina',
        labels={'Tipo_de_Maquina': 'Tipo de máquina', 'Temperatura': 'Temperatura'}
    )
    return fig


def graficodispersion(mfd):
    """Gráfico de dispersión para Vibracion vs potencia usada."""
    fig = px.scatter(
        mfd,
        x='Vibracion',
        y='Potencia_Empleada',
        title='Relación entre la Vibracion y la potencia usada',
        labels={'Vibracion': 'Vibracion', 'Potencia_Empleada': 'Potencia usada'}
    )
    return fig


