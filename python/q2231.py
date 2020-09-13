import math

num = input()
num = int(num)
for i in range(0, num):
    gen = i
    temp = i
    while temp > 0 :
        gen += temp%10
        temp/=10
        temp = math.floor(temp)
    if gen == num:
        print(i)
        break
    if i == num -1:
        print(0)