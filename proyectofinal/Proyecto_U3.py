# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Carga el set de datos especificando el delimitador
df = pd.read_csv("Laboratorio_dataset_car.csv", delimiter=";")

# Creando las barras de cada columnna
for column in df.columns:
    plt.figure(figsize=(10, 4))
    sns.countplot(data=df, x=column)
    plt.title(f"Distribución de {column}")
    plt.show()

# Se hace Encode a las caracteristicas de cada categoria
le = LabelEncoder()
df_encoded = df.apply(le.fit_transform)

# Divide los datos entre el entrenamiento y los sets de prueba
X = df_encoded.drop("class", axis=1)
y = df_encoded["class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Se inicializan los modelos
tree_model = DecisionTreeClassifier(random_state=42)
forest_model = RandomForestClassifier(random_state=42)

# Se entrenan los modelos
tree_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

# Se realizan las predicciones
tree_pred = tree_model.predict(X_test)
forest_pred = forest_model.predict(X_test)

# Se evaluan los modelos
tree_accuracy = accuracy_score(y_test, tree_pred)
forest_accuracy = accuracy_score(y_test, forest_pred)

# Se imprime la precision
print("Precision del Arbol de Decisiones: ", tree_accuracy)
print("Precision del Bosque Aleatorio: ", forest_accuracy)

# Se computa la matriz de confusion y el reporte de clasificacion de cada modelo
tree_conf_matrix = confusion_matrix(y_test, tree_pred)
forest_conf_matrix = confusion_matrix(y_test, forest_pred)

tree_class_report = classification_report(y_test, tree_pred)
forest_class_report = classification_report(y_test, forest_pred)

# Se imprimen las matricez de confusion
print("Matriz de Confusion para el Arbol de Decision:\n")
print(tree_conf_matrix)
print("\nMatriz de Confusion para el Bosque Aleatorio:\n")
print(forest_conf_matrix)

# Se imprimen los reportes de clasificacion
print("\nReporte de Clasificacion para el Arbol de Decision:\n")
print(tree_class_report)
print("\nReporte de Clasificacion para el Bosque Aleatorio:\n")
print(forest_class_report)
