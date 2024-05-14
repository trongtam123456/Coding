string = input()
#dem ki tu hoa - thuong
n_hoa = 0
n_thuong = 0
for i in string:
    if i.islower():
        n_thuong = n_thuong + 1
    else:
        n_hoa = n_hoa + 1
if n_hoa <= n_thuong:
    for i in string:
        if i.islower():
            print(i, end='')
        else:
            print(str(i).lower(), end='')
elif n_hoa > n_thuong:
    for i in string:
        if i.islower():
            print(i.upper(), end='')
        else:
            print(str(i), end='')

    
                  
    
