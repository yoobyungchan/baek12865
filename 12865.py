n, k = map(int, input().split())

w = []
v = []
for _ in range(n):
    p, q = map(int, input().split())
    w.append(p)
    v.append(q)

d = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        d[i][j] = d[i-1][j]
        if j - w[i-1] >= 0:
            d[i][j] = max(d[i][j], d[i-1][j-w[i-1]] + v[i-1])

print(d[n][k])

