#https://www.codingame.com/training/easy/temperatures
#Jan Rygulski, S16724
n = int(input())
tab = []
for i in input().split():
    t = int(i)
    tab.append(t)

number = min(tab, key=abs, default="EMPTY")
for j in range(0, len(tab), 1):
    if tab[j] == abs(number):
        number = tab[j]
if number == "EMPTY":
    print(0)
else:   
    print(number)
    
    
