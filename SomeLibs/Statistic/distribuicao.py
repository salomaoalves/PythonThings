from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import t
from scipy.stats import poisson
from scipy import stats
import matplotlib.pyplot as plt

'''PROBLEMAS UTILIZADOS (binomial):
Arremessar 5 vezes a moeda e sair cara 3 vezes'''
'''PROBLEMAS UTILIZADOS (normal):
Tirar objs q pesam < 6 (prob1); > 6 (prob2)'''
'''PROBLEMAS UTILIZADOS (t de student)
Tirar gnt q tem salario < 80 (prob1); > 80 (prob2)'''
'''PROBLEMAS UTILIZADOS (poisson)
Ocorrer 3 acidentes (prob1); menos de 3 (prob2); mais de 3 (prob3)'''

#VARIAVEIS USADAS
x = 3 #numero de sucessos (binomial)
n = 5 #numero de jogadas (binomial)
p = 0.5 #probabilidade de cada elemento ser sorteado (binomial)
u = 8 #media (normal)
dp = 2 #desvio padrao (normal)
T = 1.5 #o t, q é calculado pela formula (t de student)
grauLiberdade = 8 #grau de liberdade (t de student)
x = 3 #prob calculada (poisson)
lambdA = 2 #é a media de acidente (poisson)

#BINOMIAL
distBin = binom.pmf(x,n,p)

#NORMAL
prob1 = norm.cdf(6,u,dp)
prob2 = norm.sf(6,u,dp) #ou (1 - norm.cdf(6,u,dp))
data = norm.rvs(size = 20) #cria dados na distribuição normal
stats.probplot(data, plot=plt) #cria o grafico q-plot junto cm a linha

#T DE STUDENT
prob1 = t.cdf(T,grauLiberdade)
prob2 = t.sf(T,grauLiberdade) #ou (1 - t.cdf(T,grauLiberdade))

#POISSON
prob1 = poisson.pmf(x,lambdA)
prob2 = poisson.cdf(x,lambdA)
prob3 = poisson.sf(x,lambdA)