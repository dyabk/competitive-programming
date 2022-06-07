# CodeChef - DIV03 - Daanish and Problems
# https://www.codechef.com/LP1TO201/problems/DIV03

from sys import stdin
input = stdin.readline
T = int(input())

for _ in range(T):
    A = list(map(int, input().split()))
    K = int(input())

    for i in range(len(A) - 1, -1, -1):
        decrement = min(K, A[i])
        A[i] -= decrement
        K -= decrement
        
        if K == 0 and A[i] != 0:
            print(i + 1)
            break