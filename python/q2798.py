num, max = map(int, input().split())
card = list(map(int, input().split()))
contain = []
for i in range(0, num):
    for j in range(i+1, num):
        for k in range(j+1, num):
            contain.append(card[i]+card[j]+card[k])
minList = []
for i in range(0, len(contain)):
    if max >= contain[i]:
        minList.append(contain[i])
rst = 0
for i in range(0, len(minList)):
    if rst < minList[i]:
        rst = minList[i]
print(rst)