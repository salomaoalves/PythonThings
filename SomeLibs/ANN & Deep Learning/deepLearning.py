import matplotlib.pyplot as plt 
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist
import numpy as np

(x_treino, y_treino),(x_teste, y_teste) = mnist.load_data() #divide os dados

plt.imshow(x_treino[1],cmap='gray') #mostrar as imagens
#plt.show()

#PRÉ-PROCESSAMENTO DOS DADOS
#realiza uma reshape, ou seja, muda as dimensoes (neste caso transf cada img (q é uma matriz) numa lista)
x_treino = x_treino.reshape((len(x_treino), np.prod(x_treino.shape[1:])))
x_teste = x_teste.reshape((len(x_teste), np.prod(x_teste.shape[1:])))
#muda o tipo para float
x_treino = x_treino.astype('float32')
x_teste = x_teste.astype('float32')
#deixa os valores entre 0 e 1
x_treino /= 255
x_teste /= 255
#deixa as classe em formato dummy
y_treino = np_utils.to_categorical(y_treino, 10)
y_teste = np_utils.to_categorical(y_teste, 10)

modelo = Sequential()
modelo.add(Dense(units=64,activation='relu', input_dim=784))
modelo.add(Dropout(0.2)) #zera 20% dos neuronios
modelo.add(Dense(units=64,activation='relu'))
modelo.add(Dropout(0.2)) #zera 20% dos neuronios
modelo.add(Dense(units=64,activation='relu'))
modelo.add(Dropout(0.2)) #zera 20% dos neuronios
modelo.add(Dense(units=10, activation='softmax'))

modelo.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
historico = modelo.fit(x_treino,y_treino,epochs=20,validation_data=(x_teste,y_teste))

prev = modelo.predict(x_teste)
y_teste_matrix = [np.argmax(t) for t in y_teste]
y_prev_matrix = [np.argmax(t) for t in prev]
confusao = confusion_matrix(y_teste_matrix,y_prev_matrix)