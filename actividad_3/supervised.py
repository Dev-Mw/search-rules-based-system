# Importar las bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import graphviz


# Supongamos que tenemos un DataFrame llamado "user_data" con información de usuarios
# Este DataFrame podría tener columnas como edad, género, ingresos, etc.
# Por ejemplo, aquí simularemos un conjunto de datos de usuarios para propósitos de demostración
data = {
    'edad': [25, 30, 35, 40, 45, 50, 55, 60],
    'genero': ['Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre', 'Mujer'],
    'ingresos': [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    'cluster': [0, 1, 0, 1, 0, 1, 0, 1]  # Usar el cluster como variable objetivo
    # Añade más columnas según la información que tengas disponible
}

user_data = pd.DataFrame(data)

# Convertir características categóricas en variables numéricas usando codificación one-hot
user_data = pd.get_dummies(user_data, columns=['genero'])

# Separar las características (X) de la variable objetivo (y)
X = user_data.drop('cluster', axis=1)
y = user_data['cluster']

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo de árbol de decisión
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

# Exportar el árbol de decisión a un archivo .dot
dot_data = export_graphviz(model, out_file=None, feature_names=X.columns, class_names=['Cluster 0', 'Cluster 1'], filled=True, rounded=True)

# Crear y mostrar la visualización del árbol de decisión
graph = graphviz.Source(dot_data)
graph.render("arbol_de_decision")

# Mostrar el árbol de decisión en el notebook
graph
