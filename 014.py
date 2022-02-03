import math

n = int(input())
ans = list()

for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:
        n /= i
        ans.append(i)

if n >= 2:
    ans.append(int(n))

print(*ans)