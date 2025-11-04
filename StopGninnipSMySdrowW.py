def spin_words(sentence):
    tablica=[]
    tablica3=[]
    licznik=1
    pamiec=''
    pamiec2=''
    for i in sentence:
        tablica2=tablica
        if i!=' ':
            tablica.append(i)
        if i==' ' or licznik==len(sentence):
            
            if len(tablica2)>4:
                
                tablica2.reverse()
            tablica2.append(' ')
            for j in tablica2:
                pamiec+=j
                
            tablica2.clear()
        licznik+=1
    for i in pamiec:
        tablica3.append(i)
    tablica3.reverse()
    tablica3.pop(0)
    tablica3.reverse()
    for i in tablica3:
        pamiec2+=i
    return pamiec2