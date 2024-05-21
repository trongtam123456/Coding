# sắp xếp tăng dần theo mã ascii
# So sánh 
s = input()
t = input() # t dai hon
# chuyen s sang ascii
ascii_s = [ord(char) for char in s]
ascii_s = sorted(ascii_s)
print(ascii_s)
# chuyen s sang ascii
ascii_t = [ord(char) for char in t]
ascii_t = sorted(ascii_t)
print(ascii_t)
#in ra do dai cuoi cua s den cuoi cua t
result = ascii_t[len(ascii_s):]
print(result)
#chuyen ve lai chuoi
result = [chr(char) for char in result]
result = " ".join(result)
print(result)


