from turtle import right


def selection_sort(lista):
    '''at each step, it searches for the smallest element of the
        unordered piece and put at the beginning of the list'''
    end = len(lista)
    for i in range(end - 1): #goes through each pos looking for the smallest element
        pos_min = i
        for j in range(i+1,end): #find the smallest element and place it at the beginning
            if lista[j] < lista[pos_min]:
                pos_min = j
        lista[i],lista[pos_min] = lista[pos_min],lista[i] #make the exchange
    return lista

#------------------------------------------------------------------------------#

def bubble_sort(lista):
    '''compares adjacent elements, leaving the smallest
        smp in front; do this until the vector is sorted'''

    end = len(lista)
    
    #from end to start of the list
    for i in range(end-1,0,-1):
        changed = False #when no more changes happens
        
        #compare
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                changed = True
        
        #if it passes through the vector without making any changes, it exits the function
        if not changed:
            return lista

    return lista

#------------------------------------------------------------------------------#

def insertion_sort(lista):
    '''puts each element in its proper place,
        always leaving them in the right order'''
    
    end = len(lista)

    #starts at element 1 and goes to the last
    for i in range(1,end):
        aux = lista[i]
        j = i
        while j>0 and aux < lista[j-1]: #compares the current cm tds to its predecessors
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = aux
    return lista

#------------------------------------------------------------------------------#

def merge_sort(lista):
    '''splits the list in two, until there are lists with 1 element left, 
        groups of list pairs, already sorting them'''
    
    if len(lista) <= 1:
        return lista

    half = len(lista)//2 #to split

    #recursively, it divides each half and sorts (with the merge function)
    left_side = merge_sort(lista[:half])
    right_side = merge_sort(lista[half:])

    return merge(left_side,right_side)

def merge(left_side,right_side):
    '''aux func margeSort'''

    if not left_side: #if left is empty, return the right one
        return right_side

    if not right_side: #if right is empty, return the left one
        return left_side

    if left_side[0] < right_side[0]: #sort
        return [left_side[0]] + merge(left_side[1:],right_side)

    return [right_side[0]] + merge(left_side,right_side[1:])

#------------------------------------------------------------------------------#
import time
import random

def quick_sort(lista):
    if len(lista)<=1:
        return lista
    pivo = lista[0]
    return quick_sort([i for i in lista if i < pivo]) + \
           [i for i in lista if i == pivo] + \
           quick_sort([i for i in lista if i > pivo])

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
    bubble_sort(a)
    depois = time.time()
    print("Time of Bubble Sort is: ",depois-antes)
    
    antes = time.time()
    selection_sort(b)
    depois = time.time()
    print("Time of Selection Sort is: ",depois-antes)

    antes = time.time()
    insertion_sort(c)
    depois = time.time()
    print("Time of Insertion Sort is: ",depois-antes)

    antes = time.time()
    merge_sort(d)
    depois = time.time()
    print("Time of Merge Sort is: ",depois-antes)

    antes = time.time()
    quick_sort(e)
    depois = time.time()
    print("Time of Quick Sort is: ",depois-antes)
