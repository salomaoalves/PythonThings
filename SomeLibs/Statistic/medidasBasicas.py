import pandas as pd
import numpy as np
from scipy import stats
from database import df

#MEDIA
media = np.mean(df.iloc[:,0:4])

#MEDIANA
mediana = np.median(df.iloc[:,0])

#QUARTIS
quartis = np.quantile(df.iloc[:,0],[0,0.25,0.5,0.75,1])

#DESVIO PADRÃO
dp = np.std(df.iloc[:,0:4],ddof=1)

#RESUMO ESTATISTICO/OUTROS
resumo = stats.describe(df.iloc[:,0:4])
est = df.groupby('Estado').mean() #calcula a media (serve para count, std, .. tb), e grupo por uma coluna (Estado no caso)