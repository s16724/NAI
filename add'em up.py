#https://www.codingame.com/training/easy/addem-up
#Jan Rygulski , S16724

tab=[]
n = int(input())
for i in input().split():
   # x = int(i)
    tab.append(int(i))

tab.sort()
i = 0
cost = 0
y = n - 1
while i < y:
  
    tab.sort()
    add = tab[0] + tab [1]
    cost += add
    tab = tab[1:]
    tab[0] = add  
    i += 1

print(cost)
