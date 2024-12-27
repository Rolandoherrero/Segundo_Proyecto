import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder
import pickle

try:
    @st.cache_data
    def load_data():
        # Cargar los datos de entrenamiento desde el archivo predefinido
        data = pd.read_csv("data/machine_failure_dataset.csv")
        st.write("Vista previa del conjunto de datos cargados desde el archivo local:")
        st.dataframe(data.head())
        return data

    train_data = load_data()

    # Comprobar que el archivo tiene la columna "Failure_Risk"
    if "Failure_Risk" not in train_data.columns:
        st.error("El archivo CSV debe contener la columna 'Failure_Risk'.")
    else:
        # Separar características y etiqueta
        copia = train_data["Failure_Risk"].copy() 
        y = train_data["Failure_Risk"]
        X = train_data.drop(["Failure_Risk"], axis=1)

        # Procesar la columna target (etiquetas) usando LabelEncoder
        encoder = LabelEncoder()
        X['Machine_Type'] = encoder.fit_transform(X['Machine_Type'])

        # Dividir en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entrenar un modelo de regresión logística
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Guardar el modelo entrenado
        model_path = "models/logistic_regression_model.pkl"
        with open(model_path, "wb") as model_file:
            pickle.dump(model, model_file)

        # Realizar predicciones en el conjunto de prueba
        y_pred = model.predict(X_test)

        # Calcular métricas relevantes
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted")
        precision = precision_score(y_test, y_pred, average="weighted")
        recall = recall_score(y_test, y_pred, average="weighted")

        # Mostrar métricas utilizando st.metric
        st.title("Métricas del Modelo Entrenado")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{accuracy: .2f}", border=True)
        col2.metric("F1 Score", f"{f1: .2f}", border=True)
        col3.metric("Precision", f"{precision: .2f}", border=True)
        col4.metric("Recall", f"{recall: .2f}", border=True)

except FileNotFoundError:
    st.error(f"El archivo {csv_path} no se encontró. Verifica que exista en el folder especificado.")
except Exception as e:
    st.error(f"Ocurrió un error al procesar el archivo de entrenamiento: {e}")

# Sección para realizar predicciones
st.title("Realizar predicciones")
prediction_file = st.file_uploader("Sube un archivo CSV para realizar predicciones", type=["csv"])

if prediction_file is not None:
    try:
        # Cargar los datos del CSV de predicciones
        prediction_data = pd.read_csv(prediction_file)
        st.write("Vista previa del archivo cargado para predicciones:")
        st.dataframe(prediction_data.head())

        # Verificar si "Failure_Risk" está presente en los datos de predicción
        if "Failure_Risk" in prediction_data.columns:
            st.warning("La columna 'Failure_Risk' será ignorada para las predicciones.")
            # Guardar la copia de 'Failure_Risk' antes de eliminarla
            copia_prediccion = prediction_data["Failure_Risk"].copy()
            prediction_data = prediction_data.drop(columns=["Failure_Risk"])

        # Asegurarse de que las columnas coinciden con las del modelo
        expected_features = model.feature_names_in_
        if not all(feature in prediction_data.columns for feature in expected_features):
            missing_features = set(expected_features) - set(prediction_data.columns)
            st.error(f"El archivo CSV debe contener las siguientes columnas: {missing_features}")
        else:
            # Transformar la columna 'Machine_Type' en el conjunto de predicción
            prediction_data['Machine_Type'] = encoder.transform(prediction_data['Machine_Type'])
            
            # Realizar las predicciones
            y_pred = model.predict(prediction_data)

            st.write("Predicciones realizadas exitosamente:")
            st.dataframe(pd.DataFrame({
                "Predicción": y_pred,
            }))

            # Si el archivo contiene la columna 'Failure_Risk', calcular métricas
            if 'copia' in locals():  # Verificar si 'copia' fue guardado
                # Comparar las predicciones con la copia de la columna 'Failure_Risk'
                y_true = copia_prediccion  # Usamos la copia guardada
                accuracy = accuracy_score(y_true, y_pred)
                precision = precision_score(y_true, y_pred, average="weighted")
                recall = recall_score(y_true, y_pred, average="weighted")
                f1 = f1_score(y_true, y_pred, average="weighted")

                st.write("### Métricas del modelo en las predicciones:")
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Accuracy", f"{accuracy: .2f}")
                col2.metric("F1 Score", f"{f1: .2f}")
                col3.metric("Precision", f"{precision: .2f}")
                col4.metric("Recall", f"{recall: .2f}")
            else:
                st.warning("No se encontraron datos para comparar con 'Failure_Risk'. No se calcularán métricas.")

    except Exception as e:
        st.error(f"Ocurrió un error al realizar predicciones: {e}")
