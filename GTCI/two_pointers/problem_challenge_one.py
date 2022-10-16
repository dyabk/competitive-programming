def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()
    # reduce to triplets
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        # reduce to pairs
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            left, right = j + 1, len(arr) - 1
            while left < right:
                quad_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if quad_sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while (left < right and arr[left] == arr[left - 1]):
                        left += 1
                    while (left < right and arr[right] == arr[right + 1]):
                        right -= 1
                elif quad_sum < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
