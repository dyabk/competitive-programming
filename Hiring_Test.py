# CodeChef - HIRETEST - Hiring Test
# https://www.codechef.com/LP1TO201/problems/HIRETEST

import sys, collections
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    
    answers = []

    for i in range(N):
        line = input().rstrip()
        partial = line.count('P')
        complete = line.count('F')

        if complete >= X or complete >= (X - 1) and partial >= Y:
            answers.append("1")
        else:
            answers.append("0")

    print("".join(answers))