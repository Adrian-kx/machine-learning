import matplotlib
import matplotlib.pyplot as plt

idades = [
    23, 29, 22, 35, 42, 39, 56, 48, 33, 36, 26, 24, 28, 30, 50, 45, 41, 31, 57, 55,
    52, 47, 63, 59, 60, 38, 37, 49, 44, 43, 53, 27, 25, 34, 32, 40, 46, 58, 61, 54,
    51, 64, 62, 65, 66, 67, 29, 21, 24, 28, 26, 30, 22, 35, 31, 48, 43, 38, 39, 36,
]  # Idades dos funcionários

# Criação do histograma
plt.hist(idades, bins=[20, 30, 40, 50, 60, 70], color="dodgerblue", edgecolor="black")

# Título e rótulos dos eixos
plt.title("Distribuição de Idades no Local de Trabalho", fontsize=16)
plt.xlabel("Idade", fontsize=12)
plt.ylabel("Quantidade de Funcionários", fontsize=12)

# Adição de marcações no eixo X para as faixas etárias
plt.xticks([25, 35, 45, 55, 65])

# Exibição do histograma
plt.show()
