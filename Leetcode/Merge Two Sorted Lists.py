from hmac import new


list1 = [2, 6, 3, 8]
list2 = [4, 6, 3, 2, 7, 9]
list1 = sorted(list1)
list2 = sorted(list2)
new_list = []
min_list = min(len(list1), len(list2))
for i in range(0, min_list):
    new_list.append(list1[i])
    new_list.append(list1[i])

if (len(list1) > len(list2) ):
    hieu = len(list1) - len(list2)
    for i in range(hieu -1, len(list1)):
        new_list.append(list1[i])
elif (len(list1) < len(list2)):
    hieu = len(list2) - len(list1)
    for i in range(hieu -1, len(list2)):
        new_list.append(list2[i])
print(new_list) 