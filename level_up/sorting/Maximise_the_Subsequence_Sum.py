# CodeChef - SIGNFLIP - Maximise the Subsequence Sum
# https://www.codechef.com/LP1TO201/problems/SIGNFLIP

from sys import stdin
input = stdin.readline
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    positives = [e for e in A if e > 0]
    negatives = [-e for e in A if e < 0]

    negatives.sort(reverse=True)

    answer = sum(positives) + sum(negatives[:K])
    print(answer)