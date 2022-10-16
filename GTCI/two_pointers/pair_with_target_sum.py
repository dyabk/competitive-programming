def alternate_solution(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i

    return [-1, -1]


def pair_with_targetsum(arr, target_sum):
    l, r = 0, len(arr) - 1
    answer = [-1, -1]

    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum < target_sum:
            l += 1
        elif cur_sum > target_sum:
            r -= 1
        else:
            answer = [l, r]
            break

    return answer


def main():
    print(alternate_solution([1, 2, 3, 4, 6], 6))
    print(alternate_solution([2, 5, 9, 11], 11))


main()
