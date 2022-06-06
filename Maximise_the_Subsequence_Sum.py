# CodeChef - SIGNFLIP - Maximise the Subsequence Sum
# https://www.codechef.com/LP1TO201/problems/SIGNFLIP

from sys import stdin
input = stdin.readline
T = int(input())

from heapq import nsmallest

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    negative_count = 0
    for elem in A:
        if elem < 0:
            negative_count += 1

    positivised_portion = sum(nsmallest(min(K, negative_count), A)) * (-1)
    maxSum = positivised_portion

    for elem in A:
        if elem > 0:
            maxSum += elem

    print(maxSum)