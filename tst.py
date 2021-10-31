def check(s):
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    minus = False
    start = 0
    for i,v in enumerate(s):
        if v in d:
            start = i
            if v == '-':
                start += 1
                minus = True
            break
    new_s = s[start:]
    print(new_s)
    res = 0
    for i,v in enumerate(new_s):
        if v not in d:
            return 'Invalid no'
        res = res*10 + d[v]
    
    if minus:return -res
    return res

s = 'df42'
print(check(s))