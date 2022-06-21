import pandas as pd
import seaborn as sns

'''O modulo sklearn.datasets possui mais datasets'''
'''o modulo seaborn tem mais dataset, olhar seu repositorio no git'''

#TRABALHANDO COM OS DADOS
iris = sns.load_dataset('iris') #dados q serao usados
df = pd.DataFrame(iris) #dados na forma de um DataFrame