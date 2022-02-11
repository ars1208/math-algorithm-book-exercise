n = int(input())
a = list(map(int,input().split()))

def euclid(x,y):
    if y == 0:
        return x
    return euclid(y, x%y)

x = a[0]
y = a[1]
ans = euclid(x,y)
for i in range(2,n):
    x = ans
    y = a[i]
    ans = euclid(x,y)
print(ans)