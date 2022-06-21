import numpy as np 
from sklearn.model_selection import train_test_split
from math import ceil
from database import df

#AMOSTRAGEM SIMPLES
prob = [0.006]*149
prob.append(0.106)
amostra = np.random.choice(a=range(150),size=5,replace=False,p=prob) #(dados, tamanho, c/ ou s/ reposição, probabilidade de cada ele ser escolhido(somatoria = 1))
amostraBase = df.iloc[amostra,:] #de acordo com os numeros sorteado, selecionamos os dados correspondentes (com o index)

#AMOSTRAGEM ESTRATIZADA
x,xc,y,yc = train_test_split(df.iloc[:,0:4],df.iloc[:,4],test_size=0.95,stratify=df.iloc[:,4]) #(dados,classe,tamanho da amostra,classe)
'''(x=dados dos elementos; xc=complemento de x; y=a classe de cada elemento selecionado; yc=complemento de y)'''

#AMOSTRAGEM SISTEMÁTICA
populacao = len(df.iloc[:,0])
qtdAmostra = 5
step = ceil(populacao/qtdAmostra) #define o de quanto em quanto vai saltar (ceil faz a aproximação)
startList = np.random.randint(low=1,high=step+1,size=1) #define o primeiro elemento; retorna uma lista (begin,end,size)
start = startList[0]
sorteados = []
for i in range(qtdAmostra): #faz o vetor dos elementos escolhidos
    sorteados.append(start)
    start += step
amostraBase = df.iloc[sorteados,:] #de acordo com os numeros sorteado, selecionamos os dados correspondentes (com o index)