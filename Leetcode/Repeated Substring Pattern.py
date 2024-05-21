s = input()
n = len(s)
string_loop = ""
for i in range(0, n//2 +1 ):
    string_loop = string_loop + s[i]
    chuoi = string_loop*(n//(i+1))
    if (chuoi == s ):
        print("Chuỗi", string_loop,'lặp lại',n//(i+1),'lần')
    