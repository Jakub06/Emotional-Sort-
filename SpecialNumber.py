def special_number(number):
    number=str(number)
    album=0
    zbior=[0,1,2,3,4,5]
    for i in number:
        if int(number) in zbior:
            return 'Special!!'
        else:
            dl=len(number)
            
            for i in number:
                if int(i) in zbior:
                    album+=1 
            if album==dl:
                return 'Special!!'
            else:
                return 'NOT!!'
    pass