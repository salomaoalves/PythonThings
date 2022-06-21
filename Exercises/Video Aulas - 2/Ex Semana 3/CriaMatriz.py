def cria_matriz(nro_lin,nro_col,val):
	'''(int,int,valor) -> matriz(lista de listas)
	Cria e retorna uma matriz com nro de linha e de colunas
	em que cada elemento é igual ao valor dado.
	'''
	matriz = [] #lista vazia
	for i in range(nro_lin):
		#cria a linha i
		linha = []
		for j in range(nro_col):
			linha.append(val)
		#add linha á matriz
		matriz.append(linha)

	return matriz
