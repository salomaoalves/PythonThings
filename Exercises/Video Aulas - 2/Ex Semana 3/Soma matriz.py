import CriaMatriz

def soma_matrizes(A,B):
    nro_lin = len(A)
    nro_col = len(A[0])
    C = CriaMatriz.cria_matriz(nro_lin,nro_col,0)
    
    #faz a somatoria e atribui os valores pra matriz resultante
    for lin in range(nro_lin): #pecorre as linhas da matriz
        for col in range(nro_col): #pecorre as colunas da matriz
             C[lin][col] = A[lin][col] + B[lin][col]

    return C

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A,B))
