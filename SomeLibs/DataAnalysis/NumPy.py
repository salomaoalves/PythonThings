import numpy as np

#ARRAYS
v1 = np.array([1,2,3,4,5])#cria um array
Tipo = type(v1)
dim = v1.shape #retona o tamanho e a dimensão
v2 = np.arange(0,5,1) #cria um array com uma PA 'arange(Start,Stop,Step)'
v3 = np.zeros(10) #array com elementos 0, o paramêtro é o tamanho do array
v4 = np.linspace(0, 10, 4) #retorna um número de valores igualmente distribuídos no intervalo especificado


#MATRIZES
mat1 = np.array([[1,2,3],[4,5,6]],dtype = np.float) #cria matriz (o parametro pde ser uma lista de lista, obriga o tipo a ser float)
mat2 = np.ones((2,3)) #criando uma matriz 2x3 apenas com números "1"
mat3 = np.eye(3) #matriz com diagonal eh 1 e o resto é 0
mat4 = np.diag(np.array([1, 2, 3, 4])) #o array passado como parâmetro, forma uma diagonal
size = mat2.size #tamanho da matriz
ele = mat2[1,2] #mostrando elemento da matriz
linha = mat2[1] #motra a linha

#OPERAÇÕES PARA MATRIZES E ARRAY
typeEle = mat2.dtype #tipo dos elementos
dim2 = mat2.ndim #retorna o numero de dimensões
dim = mat1.shape #retona o tamanho e a dimensão

#OPERAÇÕES PARA ARRAY
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([4, 2, 2, 4, 4, 6, 6, 8, 8])
igual = a==b #compara cada elemento por vez
igual = np.array_equal(a, b) #compara o array como um todo
ele = b[2:9:3] #mostra os elementos (start,stop,step)
mini = a.min() #menor valor do array
maxi = a.max() #maior valor do array
a = a+2.5 #soma 2,5 em todos os elementos de a
a = np.around(a) #arredonda todos os elementos de a
c = b.flatten() #copia um array (ou 'np.copy(b)')
c1 = np.repeat(c, 3) #repetindo cada elemento de c
c2 = np.tile(c,3) #repetindo o array como um todo
conc = np.concatenate((a, b), axis=0) #concatena dois array

#ESTATISTICA
media = np.mean(v1) #calcula a media
desvPadrao = np.std(v1) #calcula o desvio padrao
var = np.var(v1) #calcula a varianca
sum = np.sum(v1) #calcula a soma
soma = v1.cumsum()#retorna a soma acumulada do array
prod = np.prod(v1) #calcula o produto


