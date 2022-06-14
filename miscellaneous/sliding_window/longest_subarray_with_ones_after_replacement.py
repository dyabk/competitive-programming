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
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()