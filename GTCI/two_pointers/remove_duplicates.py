from os import remove


def remove_duplicates(arr):
    l, r = 0, 0
    while r < len(arr):
        if arr[r] != arr[l]:
            l += 1
            arr[l] = arr[r]
        r += 1

    return l + 1


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
