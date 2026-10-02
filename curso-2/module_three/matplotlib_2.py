import matplotlib
import matplotlib.pyplot as plt
import numpy as np

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
points = [50, 55, 60, 65, 70, 75, 80, 85]

# Criação do gráfico
plt.scatter(
    study_hours,  # eixo x
    points,  # eixo y
    alpha=0.6,  # transparência do gráfico
    edgecolors="w",  # cor
    s=100,  # tamanho dos pontos
)
# plt.show()

# Cálculo da linha de tendência
z = np.polyfit(study_hours, points, 1)
p = np.poly1d(z)
plt.plot(study_hours, p(study_hours), "r--")

# título e rótulos dos eixos
plt.title("Relação entre horas de estudo e pontuação no teste", fontsize=16)
plt.xlabel("Horas de estudo", fontsize=12)
plt.ylabel("Pontuação no teste", fontsize=12)


# Adiciona GRID no fundo
plt.grid(True)

plt.show()
