def kiemtranguyento(number):
    for i in range(2, number):
        if number%i==0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))
result = []
for number in arr:
    if kiemtranguyento(number) == True:
        result.append("YES")
    else:
        result.append("NO")

# in ket qua 
for k in result:
    print(k)