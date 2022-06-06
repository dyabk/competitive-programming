# CodeChef - LAPIN - Lapindromes
# https://www.codechef.com/LP1TO201/problems/LAPIN

import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())

for _ in range(T):
    S = input().rstrip()

    middle = len(S) // 2
    if len(S) % 2 != 0:
        S = S[:middle] + S[middle+1:]

    first_half, second_half = Counter(S[:middle]), Counter(S[middle:])
    answer = "YES" if first_half == second_half else "NO"
    print(answer)