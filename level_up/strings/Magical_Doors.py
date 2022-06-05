# CodeChef - MAGDOORS - Magical Doors
# https://www.codechef.com/LP1TO201/problems/MAGDOORS

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = "1" + input().rstrip()
    ans = 0 

    for i in range(1, len(S)):
        if S[i] != S[i - 1]:
            ans += 1

    print(ans)