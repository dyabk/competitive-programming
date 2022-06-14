from collections import Counter

def non_repeat_substring(str):
  
  unique_chars = dict()
  answer = 0

  windowStart = 0
  for windowEnd in range(len(str)):
    char = str[windowEnd]
    if char in unique_chars:
      windowStart = max(windowStart, unique_chars[char] + 1)
    
    unique_chars[char] = windowEnd
    answer = max(answer, windowEnd - windowStart + 1)

  return answer

def first_solution(str):

  unique_chars = Counter()
  answer = 0

  windowStart = 0
  for windowEnd in range(len(str)):
    char = str[windowEnd]
    unique_chars[char] += 1

    substr_len = windowEnd - windowStart + 1
    while len(unique_chars) < substr_len:
      unique_chars[str[windowStart]] -= 1
      if unique_chars[str[windowStart]] == 0:
        del(unique_chars[str[windowStart]])
      windowStart += 1
      substr_len -= 1

    answer = max(answer, substr_len)

  return answer

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))

main()