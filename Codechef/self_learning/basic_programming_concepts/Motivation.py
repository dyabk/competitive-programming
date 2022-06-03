# CodeChef - IMDB - Motivation
# https://www.codechef.com/LP1TO201/problems/IMDB

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    bestRating = 0

    for i in range(N):
        S, R = map(int, input().split())
        if S <= X:
            bestRating = max(bestRating, R)
    print(bestRating)