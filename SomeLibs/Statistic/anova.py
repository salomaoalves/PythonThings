import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv('database/anova.csv',sep=';') #dados q serao utilizados

modelo1 = ols('Horas ~ Remedio',data = tratamento).fit() #cria e treina o modelo ('V.Dependente ~ V.Independente')
resul1 = sm.stats.anova_lm(modelo1) #realiza a avalição cm a anova

modelo2 = ols('Horas ~ Remedio * Sexo',data = tratamento).fit() #cria e treina o modelo ('V.Dependente ~ V.Independente * V.Independente')
resul2 = sm.stats.anova_lm(modelo2) #realiza a avalição cm a anova

mc = MultiComparison(tratamento['Horas'],tratamento['Remedio']) #faz uma comparação entre as duas variaveis
resul_test = mc.tukeyhsd() #realiza o teste TukeyHSD

grafico = resul_test.plot_simultaneous() #grafico especial para demonstrar os dados
#plt.show()