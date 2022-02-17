n = int(input())
h = list(map(int,input().split()))

ans = [0]
ans.append(abs(h[1] - h[0]))

for i in range(2,n):
    ans.append(min(ans[i-1] + abs(h[i] - h[i-1]), ans[i-2] + abs(h[i] - h[i-2])))
print(ans[-1])