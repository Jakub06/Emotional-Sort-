def reverse_fun(n):
    dl=len(n)
    tabela=[]
    counter=0
    liczba=2
    pamiec=''
    for i in n:
        tabela.append(i)
    for i in range(0,dl):
        tabela.reverse()
        print(tabela)
        pamiec+=tabela[counter]
        liczba+=1
        if liczba%2==0:
            counter+=1
    return pamiec