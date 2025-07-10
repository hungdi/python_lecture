t = int(input())
a = []
b = []
for n in range(t):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for idx in range(t):
    print(a[idx] + b[idx])
