def make_readable(seconds):
    godziny=0 
    godziny1=''
    minuty1=''
    sekundy1=''
    odpowiedz=''
    minuty=0 
    if seconds>3599:
        while seconds>3599:
            seconds=seconds-3600
            godziny+=1
    if seconds>59:
        while seconds>59:
            seconds=seconds-60
            minuty+=1
    if minuty>59:

        while minuty>59:
            minuty=minuty-60
            godziny+=1
                
    if seconds<60:
        seconds=seconds
       
    if godziny<10:
        godziny1+='0'
        godziny1+=str(godziny) 
        godziny1+=':'
    if godziny>9:
        godziny1+=str(godziny) 
        godziny1+=':'
    if minuty<10:
        minuty1+='0'
        minuty1+=str(minuty) 
        minuty1+=':'
    if minuty>9:
        minuty1+=str(minuty) 
        minuty1+=':'
    if seconds<10:
        sekundy1+='0'
        sekundy1+=str(seconds)
    if seconds>9:
        sekundy1+=str(seconds)

    odpowiedz+=godziny1
    odpowiedz+=minuty1
    odpowiedz+=sekundy1

    return odpowiedz