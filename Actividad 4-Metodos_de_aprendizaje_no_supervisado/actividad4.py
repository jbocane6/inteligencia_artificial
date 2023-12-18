import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Obtenemos los datos
data = pd.read_csv("candy-data.csv")

# Creamos una variable objetivo binaria (1 si es chocolate, 0 si no lo es)
data['is_chocolate'] = data['chocolate']

# Seleccionanos características y variable objetivo
X = data[['fruity', 'caramel', 'peanutyalmondy', 'nougat', 'crispedricewafer', 'hard', 'bar', 'pluribus']]
y = data['is_chocolate']

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializamos y entrenamos el modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Realizamos predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calculamos y mostramos la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Mostramos la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Mostramos el informe de clasificación
class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)
