def kiemtranguyento(n):
    for i in range (2, n):
        if n%i ==0:
            return "NO"
    return "YES"


n = int(input())
result = kiemtranguyento(n)
print(result)