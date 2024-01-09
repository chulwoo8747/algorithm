a = int(input())
b = 0
for i in range(a):
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    for j in range(m, n*m+1):
        if j%n == 0 and j%m == 0:
            print(j, end=' ')
            break
    for j in range(1, n+1):
        if n%j == 0 and m%j == 0:
            b = j
    print(b)