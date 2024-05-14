
def find_a(b):
    a = ""
    for i in range(0, len(b)-1, 2):
        a += b[i]
    # lay ki tu cuoi
    a += b[-1] 
    return a
t = int(input())
for _ in range(t):
    b = input()  
    print(find_a(b)) 
    
