def average_string(s):
    tabela=[]
    litery=[]
    tabela2=[]
    licznik=0
    suma=0
    odpowiedz=0
    for i in s:
        litery.append(i)
    litery.append(' ')
    if len(s)<2:
        return 'n/a'
    for i in litery:
        if i!=' ':
            tabela.append(i)
            
        else:
            licznik+=1
            if tabela[0]=='z' and tabela[1]=='e' and tabela[2]=='r' and tabela[3]=='o' and len(tabela)==4:
                tabela2.append(0)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            
            elif tabela[0]=='o' and tabela[1]=='n' and tabela[2]=='e'and len(tabela)==3:
                tabela2.append(1)
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='t' and tabela[1]=='w' and tabela[2]=='o'and len(tabela)==3:
                tabela2.append(2)
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='t' and tabela[1]=='h' and tabela[2]=='r' and tabela[3]=='e' and tabela[4]=='e' and len(tabela)==5:
                tabela2.append(3)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='f' and tabela[1]=='o' and tabela[2]=='u' and tabela[3]=='r' and len(tabela)==4:
                tabela2.append(4)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='f' and tabela[1]=='i' and tabela[2]=='v' and tabela[3]=='e' and len(tabela)==4:
                tabela2.append(5)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='s' and tabela[1]=='i' and tabela[2]=='x' and len(tabela)==3:
                tabela2.append(6)
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='s' and tabela[1]=='e' and tabela[2]=='v' and tabela[3]=='e' and tabela[4]=='n'and len(tabela)==5:
                tabela2.append(7)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='e' and tabela[1]=='i' and tabela[2]=='g' and tabela[3]=='h' and tabela[4]=='t'and len(tabela)==5:
                tabela2.append(8)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            elif tabela[0]=='n' and tabela[1]=='i' and tabela[2]=='n' and tabela[3]=='e'and len(tabela)==4:
                tabela2.append(9)
                del tabela[0]
                del tabela[0]
                del tabela[0]
                del tabela[0]
            else:
                return 'n/a'
    for i in tabela2:
        suma+=i 
    odpowiedz=int(suma/licznik)
    if odpowiedz==1:
        return 'one'
    elif odpowiedz==0:
        return 'zero'
    elif odpowiedz==2:
        return 'two'
    elif  odpowiedz==3:
        return 'three'
    elif  odpowiedz==4:
        return 'four'
    elif  odpowiedz==5:
        return 'five'
    elif  odpowiedz==6:
        return 'six'
    elif  odpowiedz==7:
        return 'seven'
    elif  odpowiedz==8:
        return 'eight'
    elif  odpowiedz==9:
        return 'nine'