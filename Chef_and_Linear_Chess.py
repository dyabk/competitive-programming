# CodeChef - TACHSTCK - Chef and Linear Chess
# https://www.codechef.com/LP1TO201/problems/LINCHESS

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P.sort(reverse = True)

    for e in P:
        if K % e == 0:
            print(e)
            break
    else:
        print(-1)