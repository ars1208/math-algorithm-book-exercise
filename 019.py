n = int(input())
a = list(map(int,input().split()))

x = a.count(1)
y = a.count(2)
z = a.count(3)

ans = (x * (x-1) + y * (y-1) + z * (z-1)) // 2

print(ans)