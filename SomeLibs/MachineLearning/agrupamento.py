import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#carregar base de dados
iris = pd.read_csv('DataBase/iris.csv')
unicos, qtd = np.unique(iris.iloc[:,4], return_counts = True)

#K-MEANS
from sklearn.cluster import KMeans

cluster = KMeans(n_clusters=3) #cria o modelo (numero de clusters)
cluster.fit(iris.iloc[:,0:4]) #treina o modelo (dados)

centroides = cluster.cluster_centers_ #centroides definidos
previsoes = cluster.labels_ #previsoes feitas
unicos2, qtd2 = np.unique(previsoes,return_counts=True) #clusters feitos; qtd em cada cluster

labelencoder = LabelEncoder() #transf os valores categoricos em numericos (faz por coluna)
iris.iloc[:,4] = labelencoder.fit_transform(iris.iloc[:,4])
confusao = confusion_matrix(iris.iloc[:,4],previsoes) #faz a matriz do confusao

#gera o grafico
plt.scatter(iris.iloc[previsoes == 0, 0], iris.iloc[previsoes == 0, 1], c='green',label = 'Setosa')
plt.scatter(iris.iloc[previsoes == 1, 0], iris.iloc[previsoes == 1, 1], c='red',label = 'Versicolor')
plt.scatter(iris.iloc[previsoes == 2, 0], iris.iloc[previsoes == 2, 1], c='blue',label = 'Virgica')
plt.legend()
#plt.show()

#FUZZY C-MEANS
import skfuzzy

r = skfuzzy.cmeans(data = iris.iloc[:,0:4].T, c=3, m=2, error=0.005, maxiter=1000, init=None) #(dados,clusters)
previsoes_porcentagem = r[2] #pega as porcentagem de cada elemento
previsoes = previsoes_porcentagem.argmax(axis = 0) #pega o maximo da porcetagem de cada elemento
resultados = confusion_matrix(iris.iloc[:,4],previsoes)

#K-MEDOIDS
from pyclustering.cluster import kmedoids
from pyclustering.cluster import cluster_visualizer

cluster = kmedoids(iris.iloc[:,0:2], [3,12,20])
cluster.get_medoids()
cluster.process()
previsoes = cluster.get_cluster() #retorna uma lista, onde cada elemento representa um cluster e contem uma lista cm os index
medoides = cluster.get_medoids() #retorna os medoides usados

v = cluster_visualizer()
v.append_clusters(previsoes,iris.iloc[:,0:2])
v.append_clusters(medoides,data=iris.iloc[:,0:2],marker='*',markersize=15)
#v.show()

l_previsoes = []
l_real = []
for i in range(len(previsoes)):
    for j in range(len(previsoes[i])):
        l_previsoes.append(i)
        l_real.append(iris.iloc[previsoes[i][j],4])
l_previsoes = np.asarray(l_previsoes)
l_real = np.asarray(l_real)
resultado = confusion_matrix(l_real,l_previsoes)