import Buscador

def criaPilha():
    '''cria uma pilha vazia'''
    pilha = []
    return pilha

def inserePilha(pilha,ele):
    '''insere um elemento na pilha'''
    pilha.append(ele)

def removePilha(pilha):
    '''remove um elemento na pilha'''
    if vaziaPilha(pilha):
        #return print("Pilha está vazia")
        return None
    return(pilha.pop())

def buscaPilha(pilha,ele):
    '''acha a posicao dum elemento na pilha'''
    pos = Buscador.buscaBinaria(pilha,ele)
    return pos

def destroiPilha(pilha):
    '''destroi um pilha, retornando um bool'''
    while len(pilha) != 0:
        removePilha(pilha)
    if vaziaPilha(pilha):
        return True
    else:
        return False

def vaziaPilha(pilha):
    '''diz se a pilha esta ou n vazia'''
    if len(pilha) == 0:
        return True
    else:
        return False
