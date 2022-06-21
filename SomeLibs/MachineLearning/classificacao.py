import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB #GaussianNB n aceita valores categoricos
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import metrics

credito = pd.read_csv('DataBase/Credit.csv',sep=',')
#print(credito.iloc[:,0])
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
naive_bayes = GaussianNB()
naive_bayes.fit(x_treino,y_treino)

previsoes = naive_bayes.predict(x_teste) #realiza a previsao
confusao = confusion_matrix(y_teste,previsoes) #cria a matriz de confusao
acuracia = accuracy_score(y_teste,previsoes) #gera a taxa de acuracia'''

#calcula os erros
mae = metrics.mean_absolute_error(y_teste, previsoes) #Mean Absolute Error (erro absoluto médio)
mse = metrics.mean_squared_error(y_teste, previsoes) #Mean Squared Error (erro médio quadrático)
rmse = np.sqrt(metrics.mean_squared_error(y_teste, previsoes)) #Root Mean Square Error (raiz do erro quadrático médio)
