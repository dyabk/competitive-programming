# CodeChef - ALPHABET - Studying Alphabet
# https://www.codechef.com/LP1TO201/problems/ALPHABET

import sys
input = sys.stdin.readline

S = set(input().rstrip())
N = int(input())

for _ in range(N):
    W = set(input().rstrip())
    answer = "No"
    if W <= S:
        answer = "Yes"

    print(answer)