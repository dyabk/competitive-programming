# CodeChef - SNAKPROC - Snake Procession
# https://www.codechef.com/LP1TO201/problems/SNAKPROC

import sys
input = sys.stdin.readline

R = int(input())

for _ in range(R):
    L = int(input())
    S = input().rstrip()

    test_letter = 'T'

    answer = "Valid"
    for c in S:
        if c == test_letter:
            answer = "Invalid"
            break
        if c == "H" or c == "T":
            test_letter = c

    if test_letter == 'H':
        answer = "Invalid"

    print(answer)