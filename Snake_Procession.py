# CodeChef - SNAKPROC - Snake Procession
# https://www.codechef.com/LP1TO201/problems/SNAKPROC

import sys
input = sys.stdin.readline

R = int(input())

for _ in range(R):
    L = int(input())
    S = input().rstrip()

    balance = 0
    is_valid = True

    for c in S:
        if c == "H":
            if balance == 0:
                balance += 1
            else:
                is_valid = False

        elif c == "T":
            if balance == 1:
                balance -= 1
            else:
                is_valid = False

    if balance != 0:
        is_valid = False

    if is_valid:
        print("Valid")
    else:
        print("Invalid")