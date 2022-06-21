import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn.tree import export_graphviz

credito = pd.read_csv('DataBase/Credit.csv',sep=',')
previsores = credito.iloc[:,0:20].values #variaveis explicatoria
target = credito.iloc[:,20].values #variaveis target

labelencoder = LabelEncoder() #transf os valores categoricos em numericos (faz por coluna)
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

#cria os data set de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(previsores,target,test_size = 0.3, random_state = 0)

#cria o modelo e treina-o
arvore = DecisionTreeClassifier()
arvore.fit(x_treino,y_treino)

#gera um codigo em tree.dot, o qual ao coloca-lo em www.webgraphviz.com, ele gera o grafo
export_graphviz(arvore, out_file='tree.dot')

previsoes = arvore.predict(x_teste) #realiza a previsao
confusao = confusion_matrix(y_teste,previsoes) #faz a matriz de confusao
acuraria = accuracy_score(y_teste,previsoes) #faz a acuracia

#gera a importancia de cada atributo na hora de fazer a predição
from sklearn.ensemble import ExtraTreesClassifier
forest = ExtraTreesClassifier()
forest.fit(x_treino,y_treino)
importancia = forest.feature_importances_