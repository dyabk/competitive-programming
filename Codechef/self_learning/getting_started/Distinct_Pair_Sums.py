# CodeChef - MANYSUMS - Distinct Pair Sums
# https://www.codechef.com/LP1TO201/problems/MANYSUMS

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    L, R = map(int, input().split())
    ans = 2 * (R - L) + 1
    print(ans)