# CodeChef - CHFSPL - Chef and Spells
# https://www.codechef.com/LP1TO201/problems/CHFSPL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    spells = [A, B, C]
    ans = sum(spells) - min(spells)
    print(ans)