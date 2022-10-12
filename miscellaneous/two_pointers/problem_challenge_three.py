def shortest_window_sort(arr):
    new_arr = sorted(arr[:])
    l, r = 0, len(arr) - 1
    while l <= r and new_arr[l] == arr[l]:
        l += 1

    while l <= r and new_arr[r] == arr[r]:
        r -= 1

    return r - l + 1
