def selectionSort(lista):
    '''a cada passo, busca o menor elemento do 
       pedaco n ordenadoe poe no inicio da lista'''
    fim = len(lista)
    for i in range(fim - 1):#passa por cada pos em busca do menor elemento
        pos_min = i
        for j in range(i+1,fim):#busca o menor elemento e coloca ele no inicio
            if lista[j] < lista[pos_min]:
                pos_min = j
        lista[i],lista[pos_min] = lista[pos_min],lista[i]#faz a troca
    return lista

#------------------------------------------------------------------------------#

def bubbleSort(lista):
    '''compara os elementos adjacentes, deixando o menor
       smp na frente; faz isso ate o vetor fique ordenado'''
    fim = len(lista)
    for i in range(fim-1,0,-1):#vai do final até o inicio
        trocou = False#caso n faça mais troca, essa variável avisa
        for j in range(i):#faz as comparações
            if lista[j] > lista[j+1]:#verifica se é maior e faz a troca
                lista[j],lista[j+1] = lista[j+1],lista[j]
                trocou = True
        if not trocou:#caso passe pelo vetor sem fazer nenhuma troca, sai da funcao
            return lista
    return lista

#------------------------------------------------------------------------------#

def insertionSort(lista):
    '''coloca cada elemento em seu devido lugar,
       smp deixando eles na ordem certa'''
    fim = len(lista)
    for i in range(1,fim):#começa no elemento 1 e vai até o ultimo
        aux = lista[i]
        j = i
        while j>0 and aux < lista[j-1]:#compara o atual cm tds os seus antecessores
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = aux
    return lista

#------------------------------------------------------------------------------#

def mergeSort(lista):
    '''divide a lista em duas, até q sobra listas cm 1 elemento,
       agrupa de pares de lista, já ordenando-as'''
    if len(lista) <= 1:#quando tem só um elemento na lista, retorna esta lista
        return lista

    meio = len(lista)//2#acha o meio pra dividir

    #de forma recursiva, vai dividindo cada metade e ordena(cm a funcao merge)
    lado_esq = mergeSort(lista[:meio])
    lado_dir = mergeSort(lista[meio:])

    return merge(lado_esq,lado_dir)

def merge(lado_esq,lado_dir):
    '''funcao auxilar da margeSort'''
    if not lado_esq:#se o lado esq for vazio, retorna o resto do lado dir
        return lado_dir

    if not lado_dir:#se o lado dir for vazio, retorna o resto do lado esq
        return lado_esq

    #faz a ordenacao
    if lado_esq[0] < lado_dir[0]:
        return [lado_esq[0]] + merge(lado_esq[1:],lado_dir)

    return [lado_dir[0]] + merge(lado_esq,lado_dir[1:])

#------------------------------------------------------------------------------#
import time
import random

def quickSort(lista):
    if len(lista)<=1:
        return lista
    pivo = lista[0]
    return quickSort([i for i in lista if i < pivo]) + \
           [i for i in lista if i == pivo] + \
           quickSort([i for i in lista if i > pivo])

#------------------------------------------------------------------------------#
import time
import random

def teste():
    a = [random.randrange(5000) for i in range(500)]
    b = a[:]
    c = a[:]
    d = a[:]
    e = a[:]
    
    antes = time.time()
    bubbleSort(a)
    depois = time.time()
    print("Tempo de Bubble Sort eh: ",depois-antes)
    
    antes = time.time()
    selectionSort(b)
    depois = time.time()
    print("Tempo de Selection Sort eh: ",depois-antes)

    antes = time.time()
    insertionSort(c)
    depois = time.time()
    print("Tempo de Insertion Sort eh: ",depois-antes)

    antes = time.time()
    mergeSort(d)
    depois = time.time()
    print("Tempo de Merge Sort eh: ",depois-antes)

    antes = time.time()
    quickSort(e)
    depois = time.time()
    print("Tempo de Quick Sort eh: ",depois-antes)
