def bouncing_ball(h, bounce, window):
    licznik=0
    if bounce>=1:
        licznik=-1
        return licznik
    if window>h:
        licznik=-1
        return licznik
    if h<=0 or bounce<=0 or window<=0 or window>h:
        licznik=-1
        return licznik
    else:
        h>window
        licznik+=1
        while h>window:
            print(h)
            licznik+=2
            h=h*bounce
        return licznik-2