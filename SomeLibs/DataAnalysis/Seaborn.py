import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#DADOS USADOS
tips = sns.load_dataset("tips")
flights_long = sns.load_dataset("flights")

#CONFIGURACOES
sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=False)
'''(size das labels/lines/outros elementos, cor dos eixos, estilo da cor dos retangulos, fonte, size fonte, ativa o palette)
ex:(notebook/paper/poster, white/dark/ticks/whitegrid, muted/bright/pastel/dark/colorblind)
{antes do grafico ser criado}'''
sns.despine(top=False, right=False, left=False, bottom=False, offset=None, trim=False) #padrao
'''(top-right-left-bottom: if true remove the line, move os retangulos dos eixos, if true tira os eixos)
{depois do grafico ser criado}'''

#FACTORPLOT

#DISTPLOT

#BOXPLOT
sns.boxplot(x="day", y="total_bill", hue="smoker", palette=["m", "g"], data=tips) 
'''(nome col no x, nome col no y, variaveis q o boxplot usa, cor(entre chaves se for + de 1) , dados)'''
plt.show()

#BARPLOT
x = np.array(list("ABCDEFGHIJ"))
y1 = np.arange(1, 11) - 5.5
sns.barplot(x=x, y=y1, palette="vlag")
'''(eixo x, eixo y, cor)'''
plt.ylabel('Variável Y') #legenda no eixo Y
plt.show()

#HEATMAP
flights = flights_long.pivot("month", "year", "passengers") #(eixo y, eixo x, valores da celulas)
sns.heatmap(flights, annot=True, fmt="d", linewidths=0.5) 
'''(pivots, aparecer os valor das celulas, ajusta os valores, size das celulas)'''
plt.show()