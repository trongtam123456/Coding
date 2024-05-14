n, k = map(int, input().split())
a = list(map(int, input().split()))

pair_found = False
if len(a)>1:
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                print(str(a[i]) + " " + str(a[j]))
                pair_found = True
                break
        if pair_found:
            break

    if not pair_found:
        print("NO")
else:
    print("NO")