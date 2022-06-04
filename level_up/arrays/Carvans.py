# CodeChef - CARVANS - Carvans
# https://www.codechef.com/LP1TO201/problems/CARVANS

import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    curMin, ans = math.inf, 0

    for i in range(N):
        if A[i] <= curMin:
            curMin = A[i]
            ans += 1

    print(ans)


