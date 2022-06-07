# CodeChef - MAXDIFF - Maximum Weight Difference
# https://www.codechef.com/LP1TO201/problems/MAXDIFF

from sys import stdin
input = stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    W = sorted(list(map(int, input().split())))

    heavier = sum(W[K:])
    heavier_k = sum(W[N - K:])

    ans = max((2 * heavier - sum(W)), 2 * heavier_k - sum(W))
    print(ans)