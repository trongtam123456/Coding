def check(strings):
    
    strings_new = ""
    for i in range(0, len(strings)):
        if strings[i] == "h" and "h" not in strings_new :
            strings_new = strings_new + "h"
            vitri = i
            break
    for k in range(vitri, len(strings)):
        if strings[k] == "e" and "e" not in strings_new :
            strings_new = strings_new + "e" 
            vitri = k 
            break
    for j in range(vitri, len(strings)):
        if strings[j] == "l" and "l" not in strings_new :
            strings_new = strings_new + "l"
            vitri = j
            break
    for m in range(vitri, len(strings)): 
        if strings[m] == "l" and strings_new.count("l") == 1 :
            strings_new = strings_new + "l"
            vitri = m
            break
    for n in range(vitri, len(strings)):     
        if strings[n] == "o" and "o" not in strings_new :
            strings_new = strings_new + "o"
            vitri = n
            break
    return strings_new

strings =  input()
if check(strings) == "hello":
    print("YES")
else:
    print("NO")

"""
=> Tối ưu hơn
def check(strings):
    target = "hello"
    target_index = 0

    for char in strings:
        if char == target[target_index]:
            target_index += 1
            if target_index == len(target):
                return True
    
    return False

strings = input().strip()
if check(strings):
    print("YES")
else:
    print("NO")
"""
