def buscaBinaria(lista,ele,pri=0,ult=None):
    '''busca um determinado valor, numa lista ordenada,
       nao por td a lista(é um upgrade da Busca Seq Ordenada)'''
    if ult == None:
        ult = len(lista)-1

    if ult < pri: #vetor vazia; elemento n esta na lista
        return False
    else:#ache o elemento do meio
        meio = pri + (ult-pri) // 2

    if lista[meio] > ele:#busca no vetor da esq
        return buscaBinaria(lista,ele,pri,meio-1)
    elif lista[meio] < ele:#busca no vetor da dir
        return buscaBinaria(lista,ele,meio+1,ult)
    else:#retorna o valor achado(sua posicao)
        return meio

#------------------------------------------------------------------------------#

def buscaSeq(lista,ele):
    '''busca um determinado valor, numa lista desordenada,
       comparando-o cm cada elemento da lista ate encontra-lo'''
    for i in range(len(lista)):#passa pelos elementos da lista
        if lista[i] == ele:
            return i
    return False

#------------------------------------------------------------------------------#

def buscaSeqOrd(lista,ele):
    '''busca um determinado valor, numa lista ordenada,
       comparando-o cm cada elemento da lista ate encontra-lo'''
    for i in range(len(lista)):#passa pelos elementos da lista
        if lista[i] == ele:
            return i
        elif ele < lista[i]:#caso o elemento buscado seja menor do q o atual, para a busca
            return False
    return False
