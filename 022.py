n = int(input())
a = list(map(int,input().split()))

ans = 0
cnt = [0] * 100000
for i in a:
  cnt[i-1] += 1

for i in range(49999):
  ans += cnt[i] * cnt[99999-i-1]
ans += cnt[49999] * (cnt[49999] - 1) // 2
print(ans)