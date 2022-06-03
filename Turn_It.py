# CodeChef - NFS - Turn It
# https://www.codechef.com/LP1TO201/problems/NFS

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    U, V, A, S = map(int, input().split())
    can_cross = U ** 2 - 2 * A * S <= V ** 2
    ans = "Yes" if can_cross else "No"
    print(ans)