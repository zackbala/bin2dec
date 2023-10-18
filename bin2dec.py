def convert_to_list(x):
    n = len(x)
    lista = []
    for i in range(n):
        temp = int(x[i]) 
        lista.append(temp)
    return lista 

def calculate(lista):
    n = len(lista)
    lista.reverse()
    soma = 0;
    temp = 0;
    for i in range(n):    
        if lista[i] == 1:
            temp = 2 ** i
            soma = soma + temp 
        if lista[i] == 0:
            soma = soma + 0
    return soma

def bin2dec(lista):
    return calculate(convert_to_list(lista)) 



