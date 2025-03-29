lista1 = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
lista2 = [2, 10, 11, 54, 21, 56, 32 ,65, 1, 65, 8]

def intersecao(lista1, lista2):
    lista1 = set(lista1)
    lista2 = set(lista2)
    intersecao = lista1 & lista2  
    return intersecao  

print(intersecao(lista1, lista2))
