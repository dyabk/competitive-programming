# CodeChef - SUBTASK - A Subtask Problem
# https://www.codechef.com/LP1TO201/problems/SUBTASK

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    if sum(A) == N:
        ans = 100
    elif sum(A[:M]) == M:
        ans = K
    
    print(ans)


    