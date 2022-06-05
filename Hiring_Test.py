# CodeChef - HIRETEST - Hiring Test
# https://www.codechef.com/LP1TO201/problems/HIRETEST

import sys, collections
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    for i in range(N):
        count = collections.Counter(input().rstrip())
        if count['F'] >= X or count['F'] >= (X - 1) and count['P'] >= Y:
            print("1", end="")
        else:
            print("0", end="")
    print("")