word1 = str(input())
word2 = str(input())
max = max(len(word1), len(word2))
#print(max)
k=0
j=0

for i in range(0, max+1):
    if (i%2==0):
        print(word1[k], end='')
        k=k+1
    if (i%2!=0):
        print(word2[j], end='')
        j=j+1


