n = int(input())

# check lucky number
def is_lucky(n):
    for digit in str(n):
        if digit not in ['4', '7']:
            return False
    return True

# Determine the divisors
def check(n):
    for i in range(1, n + 1):
        if n % i == 0 and is_lucky(i):
            return True
    return False

if check(n):
    print("YES")
else:
    print("NO")
