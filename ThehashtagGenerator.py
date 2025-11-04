def generate_hashtag(s):
    tablica=[]
    pamiec='#'
    pamiec2=''
    licznik=1
    for i in s:
        tablica.append(i.lower())
    if len(tablica)==0:
        return False
    else:
        pamiec+=(tablica[0]).upper()
        while licznik!=len(tablica):
            if tablica[licznik-1]==' ':
                pamiec+=(tablica[licznik]).upper()
            
            else:
                pamiec+=tablica[licznik]
            
            licznik+=1
        for i in pamiec:
            if i!=' ':
                pamiec2+=i
            
    if len(pamiec2)>140:
        return False
    else:
        return pamiec2