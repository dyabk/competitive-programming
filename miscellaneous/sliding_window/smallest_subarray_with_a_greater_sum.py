from math import inf

def smallest_subarray_with_a_greater_sum(s, arr):
    windowStart, windowEnd, windowSum = 0, 0, 0
    answer = inf

    for windowEnd in range (len(arr)):
        
        windowSum += arr[windowEnd]

        while windowSum >= s:
            answer = min(answer, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1

    if answer == inf:
        answer = 0

    return answer

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_a_greater_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_a_greater_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_a_greater_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_with_a_greater_sum(8, [2, 1, 5, 2, 3, 2])))

main()