def triple_double(num1, num2):
    tabela=[]
    tabela2=[]
    pamiec=[]
    pamiec2=[]
    counter=0
    counter2=0
    wynik=0
    for i in str(num2):
        tabela2.append(i)
    for i in str(num1):
        tabela.append(i)
    while counter<len(tabela2)-1:
        if tabela2[counter]==tabela2[counter+1]:
            pamiec2.append(tabela2[counter])
        counter+=1
    while counter2<len(tabela)-2:
        if tabela[counter2]==tabela[counter2+1]==tabela[counter2+2]:
            pamiec.append(tabela[counter2])
        counter2+=1
    for i in pamiec:
        for j in pamiec2:
            if i==j:
                wynik=1
            
    return wynik 