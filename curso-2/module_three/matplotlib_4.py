import matplotlib.pyplot as plt

filiais = ["Filial A", "Filial B", "Filial C", "Filial D", "Filial E"]
receita = [200, 240, 150, 400, 220]  # Receita em milhares de dólares

# Definindo as posições das barras no eixo X
posicoes = range(len(filiais))

# Criação do gráfico de barras
plt.bar(posicoes, receita, color="red", edgecolor="white")

# Adição dos nomes das filiais nas marcas do eixo X
plt.xticks(posicoes, filiais)

# Título e rótulos dos eixos
plt.title("Receita Anual por Filial", fontsize=16)
plt.xlabel("Filiais", fontsize=12)
plt.ylabel("Receita (em milhares de dólares)", fontsize=12)

# Adição de uma grade no eixo Y para facilitar a comparação das barras
plt.grid(True, axis="y", linestyle="--", alpha=0.7)

# Exibição do gráfico
plt.show()
