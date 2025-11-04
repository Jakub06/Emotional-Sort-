def open_or_senior(data):
    odp=[]
    for i in data:
        if i[0]>54 and i[1]>7:
            odp.append("Senior") 
        else:
            odp.append("Open")
    return odp