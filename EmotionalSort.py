def sort_emotions(arr, order):
    superhappy=[]
    happy=[]
    normal=[]
    sad=[]
    supersad=[]
    calosc=[]
    for i in arr:
        if i[0]!=':':
            supersad.append(i)
        else:
            if i[1]=='D':
                superhappy.append(i)
            if i[1]==')':
                happy.append(i)
            if i[1]=='|':
                normal.append(i)
            if i[1]=='(':
                sad.append(i)

    for i in superhappy:
        calosc.append(i)
    for i in happy:
        calosc.append(i)
    for i in normal:
        calosc.append(i)
    for i in sad:
        calosc.append(i)
    for i in supersad:
        calosc.append(i)
    if order==True:
        return calosc
    if order == False:
        calosc.reverse()
        return calosc