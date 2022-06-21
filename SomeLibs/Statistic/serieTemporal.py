import pandas as pd
import numpy as np 
import matplotlib.pylab as plt 
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima

#cria a base da dados
AirPassengers = '/home/salomao/Desktop/Data Science - Udemy/4 - Séries Temporais/Dados/AirPassengers.csv'
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m') #transf para tipo de date
base = pd.read_csv(AirPassengers, parse_dates=['Month'],index_col='Month',date_parser=dateparse)
ts = base['#Passengers']

#exibição e slices
ts_ano = ts.resample('A').sum() #faz a somatoria por ano
ts_mes = ts.groupby([lambda x: x.month]).sum() #faz a somatoria por mes
plt.plot(ts_mes)

#decomposição
decomposicao = seasonal_decompose(ts) #faz a decomposição
tendencia = decomposicao.trend #da tendencia
sazonal = decomposicao.seasonal #da sozonalidade
aleatorio = decomposicao.resid #da aleatoriedade
plt.subplot(4,1,1) #plotando o grafico de cada decomposiçao
plt.plot(ts, label = 'Original')
plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendencia')
plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.subplot(4,1,4)
plt.plot(aleatorio, label = 'Aleatório')
plt.tight_layout() #configurar o layout

#previsão (3 maneiras de fazer)
#1: media
ts.mean() #grande chances de erro, pois a serie n é estacionaria
ts['1960-01-01':'1960-12-31'].mean() #faz a media apenas do ultimo ano
#2: media movel
media_movel = ts.rolling(window = 12).mean() #calcula a media movel (window = subconj)
previsoes = []
for i in range(1,13): #coloca as medias das medias moveis no vetor de previsoes
    superior = len(media_movel) - i
    inferior = superior - 11
    previsoes.append(media_movel[inferior:superior].mean())
previsoes = previsoes[::-1]
plt.plot(previsoes)
#3: arima
modeo_auto = auto_arima(ts,m=12,seasonal = True, trace=True).summary() #vc acha os valores pra colocar no order abaixo (esta em SARIMAX)
modelo = ARIMA(ts, order=(2,1,2)) #cria o modelo
modelo_treinado = modelo.fit() #treina o modelo
previsoes = modelo_treinado.forecast(steps=12) #realiza as previsoes (qtd de meses previstos)
eixo = ts.plot()
start,end = '1960-01-01','1962-01-01'
modelo_treinado.plot_predict(start,end,ax=eixo,plot_insample=True) #plota e faz predição (inicio, fim /da previsao, junta os graficos)
plt.show()