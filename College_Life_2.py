# CodeChef - COLGLF2 - College Life 2
# https://www.codechef.com/LP1TO201/problems/COLGLF2

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    total_minutes = 0

    S = int(input())
    Q = list(map(int, input().split()))
    for i in range(S):
        E = list(map(int, input().split()))
        total_minutes += sum(E[1:]) - Q[i] * (len(E) - 2)

    print(total_minutes)