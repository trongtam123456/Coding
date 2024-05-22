n, k = map(int, input().split())
#convert dec to bin 
def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary_num = ''
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num
bin = str(decimal_to_binary(n)[::-1])
# dem 
def find_kth_one_position(bin, k):
    soluong = 0  
    
    for i in range(len(bin)):
        if bin[i] == '1':
            soluong += 1
            if soluong == k:
                return i 
    
    return -1 
print(find_kth_one_position(bin, k))
