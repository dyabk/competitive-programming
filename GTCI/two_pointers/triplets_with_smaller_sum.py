def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr) - 2):
        j, k = i + 1, len(arr) - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] < target:
                count += k - j
                j += 1
            else:
                k -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
