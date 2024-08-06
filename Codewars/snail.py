#                                              Чтение квадратного массива по часовой стрелке по спирали

# Мой вариант
def snail(snail_map):
    str = []
    i = len(snail_map) - 1
    q = i
    
    a = 0
    
    while i > 0:
        b = a
        c = a
        d = q
        f = q
        
        while b < q:
            str.append(snail_map[a][b])
            b += 1
        
        while c < q:
            str.append(snail_map[c][q])
            c += 1
            
        while d > a:
            str.append(snail_map[q][d])
            d -= 1
            
        while f > a:
            str.append(snail_map[f][a])
            f -= 1
        

        i -= 2
        q -= 1
        a += 1
 
    try:
        if len(snail_map) % 2 != 0:
            str.append(snail_map[q][q])
    except:
        print("Fuck you!")
    
        
    print(str)
    

# Вариант профи номер 1   
def snail_1(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


# Вариант профи номер 2  
snail = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []