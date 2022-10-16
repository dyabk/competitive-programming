def search_triplets(arr):
    triplets = []
    arr.sort()

    for i in range(len(arr) - 2):
        l, r = i + 1, len(arr) - 1
        while l < r:
            cur_sum = arr[i] + arr[l] + arr[r]
            if cur_sum == 0:
                triplets.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
                while l < r and arr[l] == arr[l - 1]:
                    l += 1
                while l < r and arr[r] == arr[r + 1]:
                    r -= 1
            elif cur_sum < 0:
                l += 1
            else:
                r -= 1

    return triplets


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
