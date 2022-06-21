import Search

def create_stack():
    '''cria uma stack vazia'''
    stack = []
    return stack

def insert_stack(stack,ele):
    '''insert a element'''
    stack.append(ele)

def remove_stack(stack):
    '''remove a element'''
    if empty_stack(stack):
        #return print("empty stack")
        return None
    return(stack.pop())

def search_stack(stack,ele):
    '''find the position of an element'''
    pos = Search.binaria_search(stack,ele)
    return pos

def destroy_stack(stack):
    '''destroy a stack'''
    while len(stack) != 0:
        remove_stack(stack)
    if empty_stack(stack):
        return True
    else:
        return False

def empty_stack(stack):
    '''says if the stack is empty or not'''
    if len(stack) == 0:
        return True
    else:
        return False
