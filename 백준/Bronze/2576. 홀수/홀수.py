hap = 0
small = 1000000000
for i in range(7):
    n = int(input())
    if n%2 != 0:
        hap += n
        small = min(small,n)
if hap == 0:
    print(-1)
else:
    print(hap,small)    