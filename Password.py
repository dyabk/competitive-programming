# CodeChef - PASSWD - Snake Procession
# https://www.codechef.com/LP1TO201/problems/PASSWD

import sys
input = sys.stdin.readline

T = int(input())

digits = set('0123456789')
lowercase_letters = set('abcdefghijklmnopqrstuvwxyz')
special_characters = set('@#%&?')
uppercase_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for _ in range(T):
    has_digit = False
    has_lowercase = False
    has_special = False
    has_uppercase = False
    is_valid = False

    S = input().rstrip()
    if len(S) >= 10:
        for i, c in enumerate(S):
            if c in lowercase_letters:
                has_lowercase = True
            if i != 0 and i != len(S) - 1 and c in uppercase_letters:
                has_uppercase = True
            if i != 0 and i != len(S) - 1 and c in digits:
                has_digit = True
            if i != 0 and i != len(S) - 1 and c in special_characters:
                has_special = True
        else:
            if has_digit and has_lowercase and has_special and has_uppercase:
                is_valid = True

    if is_valid:
        print("YES")
    else:
        print("NO")