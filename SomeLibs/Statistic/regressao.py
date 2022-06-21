import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

#DADOS USADOS
base = pd.read_csv('database/cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)
base2 = pd.read_csv('database/mt_cars.csv')
base2 = base2.drop(['Unnamed: 0'], axis = 1)
base3 = pd.read_csv('database/Eleicao.csv',sep=';')

#FAZ A CORRELAÇÃO (SIMPLES)
x = base.iloc[:,1].values #valores da variavel x (independente/target)
y = base.iloc[:,0].values #valores da variavel y (de resposta)
correlacao = np.corrcoef(x,y) #calcula a correlacoa entre a variaveis

#REGRESSAO LINEAR SIMPLES
x = x.reshape(-1,1) #reconf o elementos x (poe no formato de matriz)
modelo = LinearRegression() #cria o modelo
modelo.fit(x,y) #treina o modelo
intercecao = modelo.intercept_ #calcula a intercecao
inclinacao = modelo.coef_ #calcula a inclinação
previsao = modelo.intercept_ + modelo.coef_ * 22 #faz predicao (no caso, o 22, da variavel explanatoria)
previsao = modelo.predict(22) #faz predicao (no caso, o 22, da variavel explanatoria)
residuais = modelo._residues #retorna os residuais
'''modelo.ALGO tem funcoes q mostra coisas interessantes'''
r2 = modelo.score(x,y) #calcula o R²

#GRAFICO
plt.scatter(x,y) #cria o grafico
plt.plot(x,modelo.predict(x),color = 'red') #cria a linha

#REGRESSAO LINEAR MULTIPLA
x = base2.iloc[:,1:4].values #valores da variavel x (independente/target)
y = base2.iloc[:,0].values #valores da variavel y (de resposta)
modelo = LinearRegression() #cria o modelo
modelo.fit(x,y) #treina o modelo
r2 = modelo.score(x,y) #calcula o R²
novo = np.array([4, 200, 100]) #os valores das variaveis explanatorias
novo = novo.reshape(1,-1) #reconf o array
previsao = modelo.predict(novo) #faz predicao do valor (os valores do novo)
#para calcular o R² ajustado faz isso td, ele esta dentro das info do summary (aqui fizemos a msm coisa q em cima, só q usando comandos do R)
modelo = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base2)
modelo2 = modelo.fit()
sumario = modelo2.summary()

#REGRESSAO LOGISTICA
cor = np.corrcoef(base3.DESPESAS, base3.SITUACAO) #correlacao
x = base3.iloc[:,2].values #valores da variavel x (independente/target)
x = x[:,np.newaxis] #reconf o valores de x
y = base3.iloc[:,1].values #valores da variavel y (de respostas)
modelo = LogisticRegression() #cria o modelo
modelo.fit(x,y) #treina o modelo
intercecao = modelo.intercept_ #calcula a intercecao
inclinacao = modelo.coef_ #calcula a inclinação
basePrevisao = pd.read_csv("database/NovosCandidatos.csv",sep=';') #base para fazer as predições
despesas = basePrevisao.iloc[:,1].values #variaveis explanatoria das predições
despesas = despesas.reshape(-1,1) #reconf as variaveis
previsoesTeste = modelo.predict(despesas) #faz a predição e retorna os valores preditos
basePrevisao = np.column_stack((basePrevisao,previsoesTeste)) #insere na tabela as previsoes feitas
