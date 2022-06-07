# CodeChef - IPCCERT - Chef and IPC Certificates
# https://www.codechef.com/LP1TO201/problems/IPCCERT

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
ans = 0

for i in range(N):
    T = list(map(int, input().split()))
    ans += sum(T[:-1]) >= M and T[-1] <= 10

print(ans)