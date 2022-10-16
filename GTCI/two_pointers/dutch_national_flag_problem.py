def dutch_flag_sort(arr):
    l, h = 0, len(arr) - 1
    i = 0
    while i <= h:
        if arr[i] == 0:
            arr[i], arr[l] = arr[l], arr[i]
            i += 1
            l += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[h] = arr[h], arr[i]
            h -= 1
    return


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
