# CodeChef - PASSWD - Snake Procession
# https://www.codechef.com/LP1TO201/problems/PASSWD

import sys
input = sys.stdin.readline

T = int(input())

specials = set('@#%&?')

for _ in range(T):
    has_digit = has_lowercase = has_special = has_uppercase = False
    is_valid = False

    S = input().rstrip()
    if len(S) >= 10:
        for i, c in enumerate(S):
            if c.islower():
                has_lowercase = True
            if i > 0 and i < len(S) - 1:
                if c.isupper():
                    has_uppercase = True
                if c.isdigit():
                    has_digit = True
                if c in specials:
                    has_special = True
        else:
            if has_digit and has_lowercase and has_special and has_uppercase:
                is_valid = True

    if is_valid:
        print("YES")
    else:
        print("NO")