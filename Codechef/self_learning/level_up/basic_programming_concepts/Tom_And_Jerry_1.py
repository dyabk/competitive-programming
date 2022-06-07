# CodeChef - TANDJ1 - Tom And Jerry 1
# https://www.codechef.com/LP1TO201/problems/TANDJ1

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, c, d, K = map(int, input().split())
    dist = abs(c - a) + abs(d - b)
    if K >= dist and (K - dist) % 2 == 0:
        ans = "YES"
    else:
        ans = "NO"
    print(ans)