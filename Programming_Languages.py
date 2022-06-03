# CodeChef - PROGLANG - Programming Languages
# https://www.codechef.com/LP1TO201/problems/PROGLANG

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    ans = 0
    if (A, B) == (A1, B1) or (A, B) == (B1, A1):
        ans = 1
    elif (A, B) == (A2, B2) or (A, B) == (B2, A2):
        ans = 2
    print(ans)