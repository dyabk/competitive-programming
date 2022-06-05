# CodeChef - LAPIN - Lapindromes
# https://www.codechef.com/LP1TO201/problems/LAPIN

import sys
input = sys.stdin.readline

from collections import Counter

T = int(input())

for _ in range(T):
    S = input().rstrip()

    middle = len(S) // 2
    first = middle if len(S) % 2 == 0 else middle + 1
    A, B = Counter(S[0:middle]), Counter(S[first:len(S)])
    answer = "YES" if A == B else "NO"
    print(answer)