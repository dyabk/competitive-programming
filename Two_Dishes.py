
# CodeChef - TWODISH - Two Dishes
# https://www.codechef.com/LP1TO201/problems/TWODISH

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, A, B, C = map(int, input().split())
    first = min(A, B)
    B -= first
    second = min(B, C)
    B -= second
    ans = "YES" if N <= 0 else "NO"
    print(ans)