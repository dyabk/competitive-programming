def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = float('inf')
    for i in range(len(arr) - 2):
        l, r = i + 1, len(arr) - 1
        while (l < r):
            target_diff = target_sum - arr[i] - arr[l] - arr[r]
            if target_diff == 0:
                return target_sum
            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                l += 1
            else:
                r -= 1

    return target_sum - smallest_diff
