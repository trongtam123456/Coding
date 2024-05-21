strings = input()
s_new = ''
for i in range(-1, -len(strings), -1):
    if (strings[i] != " "):
        s_new = s_new + strings[i]
    else:
        print("The last word is", s_new[::-1], "with length", len(s_new))
        break
        

