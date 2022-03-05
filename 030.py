n, w = map(int,input().split())
loads = list()
for i in range(n):
    l = list(map(int,input().split()))
    loads.append(l)

dp = [[-1]*n, [-1]*n]

for i in range(n):
    for j in range(w):
        if j < loads[i][0]:
            dp[i][j] = dp[i-1][j]
    