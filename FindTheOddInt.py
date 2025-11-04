def find_it(seq):
    pamiec=[]
    liczby=[]
    czy=[]
    dl=len(seq)
    for i in seq:
        if str(i) in pamiec:
            continue
            
        else:
            if str(i) in str(seq):
                
                pamiec.append(str(i))
    for i in pamiec:
        counter=0
        for j in range(0,dl):
            if str(i)==str(seq[j]):
                counter+=1 
                
        liczby.append(counter)
    for i in liczby:
        if i%2==0:
            czy.append(0)
        else:
            czy.append(1)
    miejsce=czy.index(1)
    return int(pamiec[miejsce])