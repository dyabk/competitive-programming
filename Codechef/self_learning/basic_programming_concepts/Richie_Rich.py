# https://www.codechef.com/LP1TO201/problems/CHFRICH

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, X = map(int, input().split())
    ans = (B - A) // X
    print(ans)