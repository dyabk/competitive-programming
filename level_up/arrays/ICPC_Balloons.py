# CodeChef - BALLOON - ICPC Balloons
# https://www.codechef.com/LP1TO201/problems/BALLOON

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    balloons = set()

    for i, d in enumerate(A, 1):
        if 1 <= d <= 7:
            balloons.add(d)
            if len(balloons) == 7:
                print(i)
                continue
