# CodeChef - STICKS - Sticks
# https://www.codechef.com/LP1TO201/problems/STICKS

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    a, b = -1, -1

    i = 0
    while a == -1 or b == -1 and i < len(A) - 1:
        if A[i] == A[i + 1]:
            if a == -1:
                a = A[i]
            else:
                b = A[i]
            i += 2
            continue
        i += 1

    answer = a * b if a * b > -1 else -1
    print(answer)

