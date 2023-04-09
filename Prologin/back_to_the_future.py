import sys
input = sys.stdin.readline

T = int(input())

years = []

for _ in range(T):
    start, end = map(int, input().split())
    years.append([start, end])

sweep_line = []

for s, e in years:
    sweep_line.append([s, -1, 1])
    sweep_line.append([e, 1, -1])

sweep_line.sort()
print(sweep_line)

overlap = 0
answer = 0

for year, order, val in sweep_line:
    overlap += val
    print(overlap)
    answer = max(answer, overlap)

print(answer)
