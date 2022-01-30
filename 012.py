import math

n = int(input())
ans = ""

for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        ans = "No"
        break
    else:
        ans = "Yes"
print(ans)
