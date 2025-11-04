def array_diff(a, b):
    tabela1=[]
    tabela2=[]
    wartosc=1
    pamiec=[]
    pamiec2=[]
    counter=1
    if b=='':
        return a
    
    for i in a:
        tabela1.append(i)
    for i in b:
        tabela2.append(i)
    if len(tabela2)<1:
        return a
    else:
        wartosc=tabela2[0]
        dl=len(tabela1)
        for i in tabela1:
            if i not in tabela2:
                pamiec.append(int(i))

                    
            counter+=1

    for i in pamiec:
        pamiec2.append(i)
    return pamiec2