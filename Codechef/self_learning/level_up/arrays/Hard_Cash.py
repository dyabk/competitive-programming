# CodeChef - CASH - Hard Cash
# https://www.codechef.com/LP1TO201/problems/CASH

import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print(sum(A) % K)