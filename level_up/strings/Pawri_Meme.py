# CodeChef - PAWARI - Pawri Meme
# https://www.codechef.com/LP1TO201/problems/PAWRI

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S = input().rstrip()
    answer = S.replace("party", "pawri")
    print(answer)