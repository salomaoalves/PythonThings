import matplotlib as mpl
import matplotlib.pyplot as plt
versao = mpl.__version__

#para 'juntar' dois graficos, é só n colocar o show entre suas declarações#
#Dados Usados
x = [2,4,6,8,10]
y = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]

#VALE PARA TODOS OS GRAFICOS (pros do Seaborn tb)
plt.legend() #permite aparecer as legendas
plt.xlabel('Variável 1') #legenda no eixo X
plt.ylabel('Variável 2') #legenda no eixo Y
plt.title('Teste Plot') #titulo do grafico

#GRAFICOS DE LINHAS (PLOT)
plt.plot(x, y, label = 'Primeira Linha', color = 'r') #(valor no X, valor no Y, legenda, cor)
plt.plot(x2,y2, label = 'Segunda Linha', color = 'y')
plt.show() #permite aparecer o grafico (vale para tds os graficos)

#GRAFICOS DE BARRAS
plt.bar(x, y, label = 'Barras1', color = 'r') #(valor no X, valor no Y, legenda, cor)
plt.bar(x2, y2, label = 'Barras2', color = 'y')
plt.show()

#HISTOGRAMAS
plt.hist(idades, bins=12, histtype = 'bar', rwidth = 0.8) #(dados do Y, numero de barras, tipo do grafo, largura)
plt.show()
plt.hist(idades, bins=12, histtype = 'stepfilled', rwidth = 0.8) #(dados do Y, numero de barras, tipo do grafo, largura)
plt.show()

#SCATTERPLOT (grafico de pontinhos)
plt.scatter(x, y, label = 'Pontos', color = 'r', marker = 'o', s = 100) #(x,y,legenda,cor,tipo de marcacao,size da marcacao)
plt.show()

#STACK PLOTS (grafico de area)
plt.stackplot(x, y, y2, x2, colors = ['c','r','k','b'])
plt.show()

#PIE CHART (grafico de pizza)
fatias = [7, 2, 2, 13]
atividades = ['dormir','comer','trabalhar','passear']
colunas = ['c','m','r','k']
plt.pie(fatias, labels = atividades, colors = colunas, startangle = 90, shadow = True, explode = (0,0.1,0,0))
plt.show()

#DIVERSOS PLOTS
fig = plt.figure() #cria uma figure
ax1 = fig.add_subplot(1,2,1) #add um subplot na figure
ax1.plot(x, y, color='red')
ax2 = fig.add_subplot(1,2,2) #add um subplot na figure
ax2.scatter(x, y)
plt.show()

_, ax = plt.subplots(2,3) #define o tamanho, na caso, uma matriz 2x3
ax[0,1].plot(x, y, color = 'green', linestyle = '-') #define a pos e dpois o grafico
ax[1,0].hist(idades)
ax[1,2].scatter(x, y, color = 'red')
plt.show()