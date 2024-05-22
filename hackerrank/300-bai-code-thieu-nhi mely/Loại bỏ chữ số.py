def find_max_digit(tmp):
    return max(int(digit) for digit in tmp)

n = input()
tmp = n
luot = 0
while tmp != "0":
    luot += 1
    tmp = str(int(tmp) - find_max_digit(tmp))
print(luot)
