def binaria_search(lista,ele,first=0,last=None):
    '''searches for a given value, in a sorted list, not for all the list 
        (it is an upgrade of the Seq Sorted Search)'''
    
    #last element
    if last == None:
        last = len(lista)-1

    if last < first: 
        return False
    else:
        half = first + (last-first) // 2

    if lista[half] > ele:                           #search in the left vector
        return binaria_search(lista,ele,first,half-1)  
    elif lista[half] < ele:                         #search in the right vector
        return binaria_search(lista,ele,half+1,last)
    else:                                           #the value found (index)
        return half

#------------------------------------------------------------------------------#

def sequency_search(lista,ele):
    '''searches for a certain value, in an unsorted list,
        comparing it with each element of the list until it finds it'''
    
    #goes through the elements of the list
    for i in range(len(lista)):
        if lista[i] == ele:
            return i
    return False

#------------------------------------------------------------------------------#

def ordered_seq_search(lista,ele):
    '''searches for a given value in an ordered list,
        comparing it with each element of the list until it finds it'''
    
    #goes through the elements of the list
    for i in range(len(lista)):
        if lista[i] == ele:
            return i
        elif ele < lista[i]: #search failed, element not found
            return False
    return False
