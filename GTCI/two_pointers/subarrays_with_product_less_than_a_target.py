from collections import deque


def find_subarrays(arr, target):
    result = []
    left = 0
    product = 1
    for right in range(len(arr)):
        product *= arr[right]
        while (product >= target and left <= right):
            product /= arr[left]
            left += 1
        temp_list = deque()
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
