t, s = map(int, input().split())
if 0 < t and t <= 11 and s == 1 : 
    print(280)
elif t > 0 and t >= 12 and t <= 16 and s == 0:
    print(320)
else:
    print(280)