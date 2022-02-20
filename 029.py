n = int(input())

ans = [1]
ans.append(2)

for i in range(2,n):
    ans.append(ans[i-1] + ans[i-2])

if n == 1:
    print(1)
else:
    print(ans[-1])