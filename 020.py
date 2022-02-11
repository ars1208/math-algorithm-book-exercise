n = int(input())
A = list(map(int,input().split()))

ans = 0
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            for d in range(c+1,n):
                for e in range(d+1,n):
                    if A[a] + A[b] + A[c] + A[d] + A[e] == 1000:
                        ans += 1

print(ans)