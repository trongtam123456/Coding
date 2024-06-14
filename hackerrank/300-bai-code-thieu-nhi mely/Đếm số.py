a, b, c, d = map(int, input().split())
def kiemtra(x, c, d):
    if c == 0 or d == 0 :
        return False
    elif x%d!=0 and x%c!=0:
        return True 
    else:
        return False

lan = 0
for x in range(a, b+1):
    if kiemtra(x, c, d):
        lan = lan + 1
print(lan)
    
