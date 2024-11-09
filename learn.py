from sklearn.linear_model import LinearRegression
import numpy as np

# Пример данных для обучения (реальные данные должны быть более точными)
X = np.array([[1000], [950], [900], [850]])  # Исторические данные о весе
y = np.array([500, 450, 400, 350])  # Ожидаемый вес на следующих этапах

model = LinearRegression()
model.fit(X, y)

# Прогнозируем следующий вес
predicted_weight = model.predict([[870]])  # Пример для весового значения 870
print(f"Predicted weight: {predicted_weight[0]}")