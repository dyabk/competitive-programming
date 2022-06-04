# CodeChef - IPCCERT - Chef and IPC Certificates
# https://www.codechef.com/LP1TO201/problems/IPCCERT

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = sum(sum(A[i][:-1]) >= M and A[i][-1] <= 10 for i in range(N))
print(ans)