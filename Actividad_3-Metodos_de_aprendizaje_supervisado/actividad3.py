import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Cargar el DataFrame desde el archivo CSV
dataset_csv = 'Summary of Weather.csv'
df = pd.read_csv(dataset_csv)

# Imputar NaN con 0
df.fillna(0, inplace=True)

# Convertir las columnas con tipos mixtos a numéricos
cols_to_convert = ['Precip', 'WindGustSpd', 'PoorWeather', 'PRCP', 'DR', 'SPD', 'MAX', 'MIN', 'MEA', 'SNF', 'SND', 'FT', 'FB', 'FTI', 'ITH', 'PGT', 'TSHDSBRSGF', 'SD3', 'RHX', 'RHN', 'RVG', 'WTE']
df[cols_to_convert] = df[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Seleccionar características y variable objetivo
X = df[['MinTemp', 'MeanTemp']]
y = df['MaxTemp']

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = model.predict(X_test)

# Crear un DataFrame para comparar valores reales y predicciones
comparison_df = pd.DataFrame({'Real': y_test, 'Predicciones': predictions})
print(comparison_df)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Visualizar las predicciones frente a los valores reales
plt.scatter(y_test, predictions)
plt.xlabel('Valores Reales')
plt.ylabel('Predicciones')
plt.title('Predicciones vs Valores Reales')
plt.show()
