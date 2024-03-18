#https://codeforces.com/problemset/problem/520/A
def check(i):
    for i in alphabet:
        if i not in strings:
            return False
    return True    
    
n = int(input())
strings = input().lower()
alphabet = [chr(i) for i in range(97, 123)] 
result = check(alphabet)
if result == True:
    print("YES")
else:
    print("NO")
