from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Generar un conjunto de datos sintético para el transporte público
np.random.seed(0)

# Definir el número de paradas de autobús
num_paradas = 50

# Generar datos para cada parada de autobús
datos_paradas = {
    'Latitud': np.random.uniform(19.0, 20.0, num_paradas),  # Coordenadas de latitud
    'Longitud': np.random.uniform(-99.0, -98.0, num_paradas),  # Coordenadas de longitud
    'Numero_pasajeros': np.random.randint(10, 100, num_paradas),  # Número de pasajeros en la parada
    'Frecuencia_servicio': np.random.randint(1, 10, num_paradas),  # Frecuencia de servicio en minutos
    'Capacidad_vehiculos': np.random.randint(20, 100, num_paradas)  # Capacidad de los vehículos en la parada
}

# Crear DataFrame
df_transport_public = pd.DataFrame(datos_paradas)
print(df_transport_public.head())

# Inicializar y ajustar el modelo DBSCAN a los datos
dbscan = DBSCAN(eps=0.1, min_samples=5)
clusters = dbscan.fit_predict(df_transport_public[['Latitud', 'Longitud']])

# Visualizar los resultados
plt.figure(figsize=(10, 8))
plt.scatter(df_transport_public['Longitud'], df_transport_public['Latitud'], c=clusters, cmap='viridis', marker='o', s=50)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Clustering de Paradas de Autobús')
plt.colorbar(label='Grupo de Paradas')
plt.grid(True)
plt.show()

