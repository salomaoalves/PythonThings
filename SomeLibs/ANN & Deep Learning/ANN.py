from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
#import tensorflow

base = datasets.load_iris()
previsores = base['data']
classe = base['target']

classe_dummy = np_utils.to_categorical(classe) #cada linha é um elemento, e cada coluna é uma classe q esse elemento pode ser (1 pra True e 0 pra False)
x_treino, x_teste, y_treino, y_teste = train_test_split(previsores,classe_dummy,test_size=0.3,random_state=0)

modelo = Sequential() #cria um modelo sequencial, ou seja, uma camada atras da outra
modelo.add(Dense(units = 5, input_dim = 4)) #add camadas, o units representa as camadas internas, o input_dim será a camada de entras (num é a qtd de var explicatoria)
modelo.add(Dense(units=4)) #add mais uma camada interna (o num é a qtd de neuronios na camada)
modelo.add(Dense(units = 3,activation = 'softmax')) #a qtd de neuronios na camada de saida é a qtd de target, o activation sera 'softmax' quando tiver + de 2 target (é a função de ativação)

modelo.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics=['accuracy']) #compila a rede (ajusta os pesos, calcula os erros, como vc ira visualizar os resultados)
modelo.fit(x_treino,y_treino,epochs=1000,validation_data=(x_teste,y_teste)) #faz o treinamento

prev = modelo.predict(x_teste)
prev = (prev > 0.5)

y_teste_matrix = [np.argmax(t) for t in y_teste]
y_prev_matrix = [np.argmax(t) for t in prev]
confusao = confusion_matrix(y_teste_matrix,y_prev_matrix)