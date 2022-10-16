def smallest_subarray_sum(s, arr):
    start, end, _sum, answer = 0, 0, 0, float('inf')
    for end in range(len(arr)):
        _sum += arr[end]
        while _sum >= s:
            answer = min(answer, end - start + 1)
            _sum -= arr[start]
            start += 1
            
    return answer


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))

main()