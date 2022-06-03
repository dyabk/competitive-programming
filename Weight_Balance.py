# CodeChef - WEIGHTBL - Weight Balance
# https://www.codechef.com/LP1TO201/problems/WEIGHTBL

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    w1, w2, x1, x2, M = map(int, input().split())
    correct_result = x1 <= (w2 - w1) / M <= x2
    ans = 1 if correct_result else 0
    print(ans)
    