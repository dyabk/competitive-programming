# CodeChef - AVGFLEX - Average Flex
# https://www.codechef.com/LP1TO201/problems/AVGFLEX

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    answer = 0

    A.sort()

    for score in A:
        left, right = 0, N - 1

        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] <= score:
                left = mid + 1
            else:
                right = mid - 1

        better_scores = N - left
        answer += better_scores < left

    print(answer)