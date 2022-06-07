# CodeChef - TACHSTCK - Chopsticks
# https://www.codechef.com/LP1TO201/problems/TACHSTCK

from sys import stdin
input = stdin.readline

N, D = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))
L.sort()

pairs = 0

i = 0
while i <= N - 2:
    if abs(L[i + 1] - L[i]) <= D:
        pairs += 1
        i += 1
    i += 1

print(pairs)

