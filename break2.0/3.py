n = int(input())
for i in range(n):
    x = int(input())
    if x % (i + 1) == 0:
        print(x)