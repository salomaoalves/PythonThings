#MAP
list(map(FUNCAO,LISTA))
'''ela mapeia os elementos de uma lista por meio de uma funcao'''
'''lista: uma seq de alguma coisa
   funcao: alguma funcao, pode ser lambda'''
'''se a funcao for lambda, ela pode aceitar mais de uma lista,
ex: list(map(lambda x,y:x+y, a, b)), onde ela soma os elementos
da lista a com seu respectivo elemento da lista b'''

#FILTER
list(filter(FUNCAO,LISTA))
'''ela filtra elementos de uma lista por meio de uma funcao'''
'''lista: uma seq de alguma coisa
   funcao: alguma funcao, pode ser lambda'''

#REDUCE
list(reduce(FUNCAO,LISTA))
'''ela reduz uma lista, de acordo com uma funcao'''
'''para usa-la, devemos importa o modulo functools'''
'''lista: uma seq de alguma coisa
   funcao: alguma funcao, pode ser lambda'''

#LIST COMPREHENSIONS
lst = [VAR for VAR in LISTA if COND]
'''assim, VAR pega os elementos da LISTA, verifica a condição e 
depois poe na lista; no primeiro VAR, pode-se fazer qualquer
operacao aritmetica, e ele pode ser um numero; a condicao é opcional'''
'''pode-se fazer aninhamentos'''

#ZIP
list(zip(LISTA1,LISTA2))
'''agrega valores de 2 seq e retorna uma lista, onde cada elemento é
uma tupla de pares, ou seja, ele junta cada elemento da lista1 com seu
respectivo elemento da lista2; o numero de tuplas sera sempre igual ao
tamanho da menos lista'''
'''Ex: list(zip([1,2,3,4],[1,2,3])) => [(1,1),(2,2),(3,3)]'''

#ENUMARATE
list(enumerate(LISTA))
'''recebe uma lista, e retorna uma lista, onde cada elemento é uma tupla
de pares, onde cada par é formado pelo indice de cada valor e o proprio
valor'''
'''Ex: list(enumarete([10,20,30])) => [(0,10),(1,20),(2,30)]'''