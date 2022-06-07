# CodeChef - EQUINOX - Equinox Strings
# https://www.codechef.com/LP1TO201/problems/EQUINOX

import sys
input = sys.stdin.readline

T = int(input())

word = set("EQUINOX")

for _ in range(T):
    N, A, B = map(int, input().split())

    sarthak = anuradha = 0

    for i in range(N):
        S = input().rstrip()[0]
        if S in word:
            sarthak += A
        else:
            anuradha += B

    ans = "DRAW"
    if sarthak > anuradha:
        ans = "SARTHAK"
    elif sarthak < anuradha:
        ans = "ANURADHA"

    print(ans)

