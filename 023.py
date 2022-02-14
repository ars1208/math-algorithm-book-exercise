n = int(input())
b = list(map(int,input().split()))
r = list(map(int,input().split()))

ans = 0
for i in range(n):
    ans += b[i]
for j in range(n):
    ans += r[j]

print(ans / n)