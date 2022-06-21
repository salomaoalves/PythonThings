import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[41,34],[18,7]]) #dados utilizados
print(chi2_contingency(novela)) #o segundo parametro retornado é o value-p
