from collections import Counter

def longest_substring_with_k_distinct(str1, k):
  unique_characters = Counter()
  answer = 0

  windowStart = 0
  for windowEnd in range(len(str1)):
    char = str1[windowEnd]
    if char not in unique_characters:
      unique_characters[char] = 0
    unique_characters[char] += 1

    while len(unique_characters) > k:
      unique_characters[str1[windowStart]] -= 1
      if unique_characters[str1[windowStart]] == 0:
        del(unique_characters[str1[windowStart]])
      windowStart += 1

    answer = max(answer, windowEnd - windowStart + 1)

  return answer

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()