# CodeChef - CM164364 - Chocolate Monger
# https://www.codechef.com/LP1TO201/problems/CM164364

from sys import stdin
from collections import Counter

input = stdin.readline
T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    types = len(set(A))
    repeated = n - types

    x -= repeated
    answer = types if x <= 0 else types - x
    print(answer)