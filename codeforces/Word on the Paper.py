a = int(input())
result_list = []

for _ in range(a):
    temp_list = []
    for _ in range(8):
        x = input()
        temp_list.append(x)
    
    # Splitting temp_list into chunks of 64 elements
    chunked = [temp_list[i:i+64] for i in range(0, len(temp_list), 64)]
    result_list.append(chunked)

for chunks in result_list:
    strings = ""
    for chunk in chunks:
        strings += ''.join(item for item in chunk if item != ".")
    print(strings)
