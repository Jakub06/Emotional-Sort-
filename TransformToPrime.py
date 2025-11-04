from math import sqrt
def pierwsza(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def minimum_number(numbers):
    suma=sum(numbers)
    while pierwsza(suma) != True:
        suma+=1 
    return suma-sum(numbers)