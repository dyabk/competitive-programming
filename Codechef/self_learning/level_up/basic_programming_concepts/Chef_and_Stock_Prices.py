# CodeChef - CSTOCK - Chef and Stock Prices
# https://www.codechef.com/LP1TO201/problems/CSTOCK

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    S, A, B, C = map(int, input().split())
    new_price = S * (1 + C/100)
    answer = "Yes" if A <= new_price <= B else "No"
    print(answer)