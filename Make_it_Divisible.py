# CodeChef - MAKEDIV3 - Make It Divisible
# https://www.codechef.com/LP1TO201/problems/MAKEDIV3

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = input().rstrip()

    start = 10 ** (int(N) - 1)
    end = 10 ** int(N)

    for X in range(start, end):
        if X % 2 != 0 and X % 3 == 0 and X % 9 != 0:
            print(X)
            break

