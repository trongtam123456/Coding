def find(lst):
    lst_money = {0}  # Use a set for efficient duplicate checking
    for item in lst:
        for item_lst_money in list(lst_money):  # Create a copy for iteration
            lst_money.add(item_lst_money + item)
    return sorted(lst_money)  # Return a sorted list for consistency

n = int(input())
lst = list(map(int, input().split()))
lst2 = find(lst)
print(lst2)
result = []
for i in range(0, max(lst)):
    if i not in lst2:
        result.append(int(i))
print(min(result))
### CHƯA XONG