# CodeChef - PROGLANG - Programming Languages
# https://www.codechef.com/LP1TO201/problems/PROGLANG

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    one = (A1, B1)
    two = (A2, B2)
    
    ans = 0
    if A in one and B in one:
        ans = 1
    elif A in two and B in two:
        ans = 2
    print(ans)