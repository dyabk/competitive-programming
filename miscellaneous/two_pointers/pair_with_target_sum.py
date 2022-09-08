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
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
