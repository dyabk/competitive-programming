# https://www.codechef.com/LP0TO101/problems/FLOW001

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)