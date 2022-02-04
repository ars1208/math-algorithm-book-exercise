a, b = map(int, input().split())

def euclid(x,y):
    if y == 0:
        return x
    return euclid(y, x%y)

print(euclid(a,b))