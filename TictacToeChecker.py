def is_solved(board):
    licznik=0
    tabela1=[]
    tabela2=[]
    tabela3=[]
    wygrana=-1
    for i in board[0]:
        tabela1.append(i)
    for i in board[1]:
        tabela2.append(i)
    for i in board[2]:
        tabela3.append(i)
    if tabela1[0]==1 or tabela1[0]==2:
        if tabela1[0]==tabela1[1]==tabela1[2]:
            wygrana=tabela1[0]
            return wygrana
            licznik+=1
    if tabela2[0]==1 or tabela2[0]==2:
        if tabela2[0]==tabela2[1]==tabela2[2]:
            wygrana=tabela2[0]
            return wygrana
            licznik+=1
    if tabela3[0]==1 or tabela3[0]==2:
        if tabela3[0]==tabela3[1]==tabela3[2]:
            wygrana=tabela3[0]
            return wygrana
            licznik+=1
    if tabela1[0]==1 or tabela1[0]==2:
        if tabela1[0]==tabela2[0]==tabela3[0]:
            wygrana=tabela1[0]
            return wygrana
            licznik+=1
    if tabela1[1]==1 or tabela1[1]==2:
        if tabela1[1]==tabela2[1]==tabela3[1]:
            wygrana=tabela1[1]
            return wygrana
            licznik+=1
    if tabela1[2]==1 or tabela1[2]==2:
        if tabela1[2]==tabela2[2]==tabela3[2]:
            wygrana=tabela1[2]
            return wygrana
            licznik+=1
    if tabela1[0]==1 or tabela1[0]==2:
        if tabela1[0]==tabela2[1]==tabela3[2]:
            wygrana=tabela1[0]
            return wygrana
            licznik+=1
    if tabela1[2]==1 or tabela1[2]==2:
        if tabela1[2]==tabela2[1]==tabela3[0]:
            wygrana=tabela1[2]
            return wygrana
            licznik+=1
    if licznik==0:
        if 0 in tabela1 or 0 in tabela2 or 0 in tabela3:
            return wygrana
        else:
            wygrana=0
            return wygrana