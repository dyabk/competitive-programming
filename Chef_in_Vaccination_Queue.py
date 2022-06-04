# CodeChef - VACCINQ - Chef in Vaccine Queue
# https://www.codechef.com/LP1TO201/problems/VACCINQ

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, P, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(P):
        answer += X if A[i] == 0 else Y
    print(answer)