acc = ["a", "b", "c", "d"]
money = [[5, 10], [5, 20, 41], [2, 6, 70, 4], [6, 5]]
#tinh tong tien cua tung ong
list_money = []
for i in range(0, len(money)):
    tong = 0
    for k in range(0, len(money[i])):
        tong = tong + money[i][k]
    list_money.append(tong)
list_money1 = sorted(list_money)
# kiem tra xem lon nhat
for j in range(0, len(list_money)):
    if list_money1[len(list_money1)-1] == list_money[j]:
        print('ong', acc[j], 'nhieu tien nhat voi tong tien la', list_money[j])
        break
