def sum_two_smallest_numbers(numbers):
    tabela=[]
    for i in numbers:
        tabela.append(i)
    tabela.sort()
    jeden=tabela[0]
    dwa=tabela[1]
    suma=jeden+dwa
    return suma