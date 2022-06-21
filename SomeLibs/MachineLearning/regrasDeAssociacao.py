import pandas as pd
from apyori import apriori

#DADOS
dados = pd.read_csv('DataBase/transacoes.txt',header=None)

#APRIORI
#deixando eles no formato de listas, onde cada elemento é uma transação
transacoes = []
for i in range(0,6): #range defino pela qtd de transações
    transacoes.append([str(dados.values[i,j]) for j in range(0,3)]) #range definido pela qtd max de items

#crianção das regras
regras = apriori(transacoes, min_support = 0.5, min_confidence = 0.5) #gera um obj de regras (suporte, confiança)

#cada resultado é um jeito de ver a regras, o 2 e 3 são os melhores
resultados = list(regras)
resultados2 = [list(x) for x in resultados]
resultados3 = []
for j in range(0,7): #range definido pela qtd de regras criadas
    resultados3.append([list(x) for x in resultados2[j][2]])
