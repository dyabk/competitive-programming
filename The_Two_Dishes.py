import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    maxDif = 0
    N, S = map(int, input().split())
    ans = S if N >= S else N - (S - N)
    print(ans)