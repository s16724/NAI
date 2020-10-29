#https://www.codingame.com/training/easy/horse-racing-duals
#Jan Rygulski, S16724
import sys
n = int(input())
P = []
for i in range(n):
    P.append(int(input()))
P.sort()
D =P[0]
for i in range(1, n):
    D = min(D,P[i] - P[i - 1])

print(D)


