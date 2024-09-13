def likes(names):
    etc = []
    if not names:
        return "no one likes this"
    
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        names.insert(1,"and")
        return f'{(" ").join(names)} like this'
    elif len(names) == 3:
        names[0] =  f'{names[0]},'
        names.insert(2,"and")
        return f'{(" ").join(names)} like this'
    else:
        names[0] =  f'{names[0]},'
        names.insert(2,"and")
        return f'{(" ").join(names[:3])} {len(names[3:])} others like this'
        
        
        