"""
Để sắp xếp một xâu thành một xâu đối xứng có thứ tự từ điển nhỏ nhất, ta có thể làm theo các bước sau:

1. Kiểm tra điều kiện khả thi: Đầu tiên, kiểm tra xem xâu có thể sắp xếp thành xâu đối xứng hay không. Một xâu có thể sắp xếp thành xâu đối xứng nếu và chỉ nếu số lượng ký tự xuất hiện lẻ không quá 1 (vì ở giữa xâu đối xứng chỉ có thể có tối đa một ký tự lẻ).

2. Tạo một phần của xâu đối xứng: Đếm tần suất xuất hiện của mỗi ký tự trong xâu. Chia các ký tự này vào hai phần bằng nhau (một phần sẽ là nửa đầu và một phần sẽ là nửa cuối của xâu đối xứng). Nếu có một ký tự xuất hiện lẻ, ký tự này sẽ được đặt ở giữa xâu đối xứng.

3. Ghép các phần lại với nhau: Tạo xâu đối xứng bằng cách ghép nửa đầu, ký tự lẻ (nếu có), và nửa cuối (là phần đảo ngược của nửa đầu) lại với nhau.
"""
from collections import Counter

def kiemtradoixung(s):
    soluong = 0
    counter = Counter(s)
    for item in counter.values():
        if item%2!=0:
            soluong = soluong + 1
        if soluong >= 2:
            return False
    return True       
def chuoi_doi_xung(s):
    ki_tu_le = ""
    counter = Counter(s)
    doi_xung_1 = []
    doi_xung_2 = []
    for char in sorted(counter.keys()):
        count = counter[char]
        doi_xung_1.append(char * (count // 2))
        if count % 2 != 0:
            ki_tu_le = char
    doi_xung_1 = ''.join(doi_xung_1)
    doi_xung_2 = doi_xung_1[::-1]
    return doi_xung_1 + ki_tu_le + doi_xung_2

s = input()
#print(chuoi_doi_xung(s))
if kiemtradoixung(s):
    print(chuoi_doi_xung(s))

else:
    print("NO SOLUTION")



