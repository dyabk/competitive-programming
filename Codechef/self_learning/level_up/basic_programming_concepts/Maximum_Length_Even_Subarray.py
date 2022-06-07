# CodeChef - MXEVNSUB - Maximum Length Even Subarray
# https://www.codechef.com/LP1TO201/problems/MXEVNSUB

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    _sum = N * (1 + N) // 2
    ans = N if _sum % 2 == 0 else N - 1
    print(ans)