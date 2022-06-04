# CodeChef - IPCCERT - Chef and IPC Certificates
# https://www.codechef.com/LP1TO201/problems/IPCCERT

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [[]]
for i in range(N):
    A.append([0] + list(map(int, input().split())))

ans = 0

for i in range(1, N + 1):
    if A[i][-1] <= 10:
        _sum = 0    
        for j in range(1, K + 1):
            _sum += A[i][j]
        if _sum >= M:
            ans += 1

print(ans)