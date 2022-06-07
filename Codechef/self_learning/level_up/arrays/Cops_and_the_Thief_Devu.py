# CodeChef - COPS - Cops and the Thief Devu
# https://www.codechef.com/LP1TO201/problems/COPS


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, x, y = map(int, input().split())
    
    distance = x * y
    houses = [False] + [True] * 100
    house_numbers = list(map(int, input().split()))
    
    for num in house_numbers:
        left = max(num - distance, 0)
        right = min(num + distance + 1, len(houses))
        for i in range(left, right):
            houses[i] = False

    answer = sum(houses)
    print(answer)

