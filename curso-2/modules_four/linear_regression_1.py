from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Carregando o conjunto de dados diabetes
diabetes = load_diabetes()

# Separando as variáveis independentes (X) e a variável alvo (y)
X = diabetes.data[:, 2]  # Usando apenas uma característica para fins de visualização
y = diabetes.target

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando o modelo de regressão linear
model = LinearRegression()

# Treinando o modelo com os dados de treinamento
model.fit(X_train.reshape(-1, 1), y_train)

# Fazendo previsões com os dados de teste
y_pred = model.predict(X_test.reshape(-1, 1))

# Plotando o gráfico de dispersão dos dados de teste
plt.scatter(X_test, y_test, color='blue', label='Dados de Teste')

# Plotando a linha de regressão
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linha de Regressão')

# Adicionando rótulos e título ao gráfico
plt.xlabel('Característica')
plt.ylabel('Progressão da Doença')
plt.title('Regressão Linear - Diabetes')
plt.legend()

# Exibindo o gráfico
plt.show()
