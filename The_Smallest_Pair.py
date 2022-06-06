# CodeChef - SMPAIR - The Smallest Pair
# https://www.codechef.com/LP1TO201/problems/SMPAIR

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print(sum(sorted(a)[:2]))