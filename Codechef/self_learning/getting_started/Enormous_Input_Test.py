import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0

for _ in range(n):
    number = int(input())
    ans += number % k == 0

print(ans)