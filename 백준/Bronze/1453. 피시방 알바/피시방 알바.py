a = int(input())
list = []
num = 0
jari = input().split()
for i in range(a):
    if jari[i] not in list:
        list.append(jari[i])
    else:
        num +=1
print(num)