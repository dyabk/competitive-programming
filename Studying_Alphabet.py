# CodeChef - ALPHABET - Studying Alphabet
# https://www.codechef.com/LP1TO201/problems/ALPHABET

import sys
input = sys.stdin.readline

S = input().rstrip()
can_read = set(S)

N = int(input())

for i in range(N):
    W = input().rstrip()
    ans = "Yes"
    for c in W:
        if c not in can_read:
            ans = "No"
            break

    print(ans)


