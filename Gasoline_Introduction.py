# CodeChef - BEGGASOL - Gasoline Introduction
# https://www.codechef.com/LP1TO201/problems/BEGGASOL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    f = list(map(int, input().split()))
    gas = f[0]

    for i, g in enumerate(f[1:]):
        if gas > 0:
            gas += g - 1
        else:
            print(sum(f[:i]))
            break
    else:
        print(sum(f))