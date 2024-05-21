def signFunc(x):
    tich = 1
    for i in range(0, len(x)):
        tich = tich*x[i]
    if tich<0:
        return -1
    elif tich>0:
        return 1
    else: 
        return 0
    

x = [5, 6, -7, -8, 9, 10, -20]
print(signFunc(x))
