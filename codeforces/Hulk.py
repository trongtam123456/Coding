strings = "I hate"
a = int(input())
if a>=2:
    for i in range(2, a+1):
        if i % 2 == 0:
            strings = strings + " that I love"
        else:
            strings = strings + " that I hate"

print(strings + " it")