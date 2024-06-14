testcase = int(input())
result = []
for i in range(0, testcase):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    keo = 0
    for buatiec in lst:
        if m%(buatiec+1) == 0:
            keo = keo + int(m/(buatiec+1))
        else:
            if (m/buatiec>0):
                keo = keo + (m%(buatiec+1)) + int(m/(buatiec+1))
            else:
                keo = keo + m
    result.append(keo)
for keo in result:
    print(keo)


