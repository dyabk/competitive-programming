# CodeChef - SMOL - Smallest Possible Whole Number
# https://www.codechef.com/LP1TO201/problems/SMOL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    ans = N if K == 0 else N % K
    print(ans)