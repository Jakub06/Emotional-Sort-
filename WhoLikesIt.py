def likes(names):
    dl=len(names)
    if dl==0:
        return 'no one likes this'
    elif dl==1:
        return f'{names[0]} likes this'
    elif dl==2:
        return f'{names[0]} and {names[1]} like this'
    elif dl==3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif dl>3:
        return f'{names[0]}, {names[1]} and {dl-2} others like this'
    pass