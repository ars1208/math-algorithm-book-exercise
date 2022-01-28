n = int(input())
ans = list()

for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        ans.append(str(i))
print(" ".join(ans))
