my_list = [4, 4, 3, 7, 9, 1]
#chuyen ve strings
noi = ''
strings_list = noi.join(map(str, my_list))
# chuyen ve int
strings_list = int(strings_list)
strings_list = strings_list + 1
strings_list = str(strings_list)
strings_list = [int(i) for i in strings_list]
print(strings_list)