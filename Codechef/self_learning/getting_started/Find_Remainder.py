# https://www.codechef.com/LP0TO101/problems/FLOW002

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(a % b)