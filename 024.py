n = int(input())
pq_list = list()
for i in range(n):
    pq = list(map(int, input().split()))
    pq_list.append(pq)
ans = 0

for j in pq_list:
    ans += j[1] / j[0]

print(ans)