# CodeChef - CSUB - Count Substrings
# https://www.codechef.com/LP1TO201/problems/CSUB

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().rstrip()

    ones, answer = 0, 0

    for number in S:
        if number == "1":
            ones += 1
            answer += ones

    print(answer)