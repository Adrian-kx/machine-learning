from sklearn.cluster import KMeans

# Dados de exemplo para o argumento
x = [[6, 7], [2, 1], [3, 2], [8, 9]]

# Instanciação de uma estimator KMeans
kmeans = KMeans(n_clusters=2, n_init=10)

# Treinando o modelo
kmeans.fit(x)

print(kmeans.cluster_centers_)