n = int(input())
a = list(map(int,input().split()))

c_100 = 0
c_200 = 0
c_300 = 0
c_400 = 0
for i in range(n):
  if a[i] == 100:
    c_100 += 1
  elif a[i] == 200:
    c_200 += 1
  elif a[i] == 300:
    c_300 += 1
  elif a[i] == 400:
    c_400 += 1

print(c_100 * c_400 + c_200 * c_300)