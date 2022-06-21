import pandas as pd
from pandas import Series
from pandas import DataFrame
versao = pd.__version__ #verson do pandas

#DADOS
dict = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}
esportes = ['Futebol', 'Tenis', 'Natação', 'Basktetball']
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'], 'Ano': [2002, 2003, 2004, 2005, 2006], 'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame({'Dias':[1, 2, 3, 4, 5, 6, 7],'Visitantes':[45, 23, 67, 78, 23, 12, 14],'Taxas':[11, 22, 33, 44, 55, 66, 77]})

#SERIES
#criando series
obj = Series([67, 78, -56, 13]) #criando uma serie sem indice
obj2 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd']) #cria uma serie definindo os indices
obj3 = Series(dict) #cria uma serie apartir dum dict
obj4 = Series(dict,index=esportes) #criz uma serie, faz um match entre os indices do dict e a lista do esporte, se n der match, o valor é NaN
#operações em series
values = obj.values #retorna os valores
indice = obj.index #retorna o indices
pedaco = obj2[obj2 > 3] #pega só os valores maiores q 3
ele = obj2['b'] #pega apenas o valor do indice 'b'
contido = 'd' in obj2 #verifica se o indice esta contido no obj
nulos = pd.isnull(obj4) #retorna se ha nulos (ou usa esse 'obj4.isnull()')
nnulos = pd.notnull(obj4) #retona se n ha nulos
conc = obj3 + obj4 #concatena, se der match nos index, soma os valores, se n, o valor é NaN
obj4.name = 'população' #muda o nome da serie
obj4.index.name = 'esporte' #muda o nome dos index da serie

#DATAFRAME
#criando df
df = DataFrame(data) #cria um DataFrame, podemos altera\add columas e altera os index, como no ex abaixo
df2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'], index = ['um', 'dois', 'três', 'quatro', 'cinco'])
df3 = DataFrame([['Santa Catarina',2002,1.5],['Parana',2003,1.7]]) #criando DataFrame com lista de lista
#operacao em df
col = df2['Estado'] #retorna apenas uma coluna (ou usa 'df2.Estado')
colunas = df2.columns #retorna as colunas (ou 'list(df2)')
df2['species'] = pd.Categorical.from_codes([0,1,2,2,3], ['A','B','C','D']) #add uma nova coluna, 1 Array tem o msm num de linhas q o df atribui cada valor a uma linha, o 2 Array relaciona cada elemento com o num do 1 Array
df2['numeros'] = [x for x in range(5)] #add uma nova coluna, porém o array tem o msm tamanho do numero de linhas do df
ind = df2.index #retorna os index
loc1 = df2.loc['quatro'] #localizo a coluna
loc2 = df2.iloc[2] #localizo o index
df = df.set_index('Estado') #coloca a coluna Estado como index
val = df2.values #retorna os valores
val = df2.Estado.value_counts() #retorna a qtd de valores de cada coluna
val = df2.Estado.value_counts().index #retorna os valores de cada coluna, sem repeti-los
trans = df2.T #transforme linhas e colunas em colunas e linhas
tipo = df2.dtypes #retorna o tipo de cada coluna
sli = df2[:2] #faz um slice (start,stop,step)
copia = df2.copy() #faz uma copia do DataFrame
topo = df2.head() #mostra o topo
nulos = pd.isnull(df2) #retorna se ha nulos (ou usa esse 'df2.isnull()')(df2.isnull().sum() soma os valores null de cada coluna)
nnulos = pd.notnull(df2) #retona se n ha nulos (ou usa esse 'df2.notnull()')
correlacao = df2.corr() #mostra a correlacao entres as variaveis (0=n ha correlacao; +1=forte correlaçao positiva{diretamente proporcional}; -1=forte correlacao negativa{inversamente proporcional})