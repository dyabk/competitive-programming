def only_one_count(arr, k):

    window_start, max_ones_count, answer = 0, 0, 0

    for window_end in range(len(arr)):
        digit = arr[window_end]
        if digit == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1

        answer = max(answer, window_end - window_start + 1)

    return answer


def length_of_longest_substring(arr, k):
  binCount = [0, 0]
  answer = 0

  windowStart = 0
  for windowEnd in range(len(arr)):
    digit = arr[windowEnd]

    binCount[digit] += 1

    while binCount[0] > k:
      binCount[arr[windowStart]] -= 1
      windowStart += 1

    answer = max(answer, windowEnd - windowStart + 1)

  return answer

def main():
  print(only_one_count([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(only_one_count(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()