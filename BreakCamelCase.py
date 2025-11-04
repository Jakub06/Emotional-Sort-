def solution(s):
    tabela=[]
    pamiec=''
    for i in s:
        tabela.append(i)
    for i in tabela:
        if i!=i.upper():
            pamiec+=i 
        else:
            pamiec+=' '
            pamiec+=i 
    return pamiec    