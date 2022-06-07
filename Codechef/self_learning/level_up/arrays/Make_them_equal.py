# CodeChef - MAKEEQUAL - Make them equal
# https://www.codechef.com/LP1TO201/problems/MAKEEQUAL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    minOps = max(A) - min(A)
    print(minOps)
