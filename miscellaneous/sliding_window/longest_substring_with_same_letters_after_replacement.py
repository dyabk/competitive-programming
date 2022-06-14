from collections import Counter

def length_of_longest_substring(str1, k):
  
  letterCount = Counter()
  maxRepeatLetterCount = 0
  windowStart = 0
  answer = 0

  for windowEnd in range(len(str1)):
    letter = str1[windowEnd]
    letterCount[letter] += 1
    maxRepeatLetterCount = max(maxRepeatLetterCount, letterCount[letter])
    
    if(windowEnd - windowStart + 1 - maxRepeatLetterCount) > k:
      char = str1[windowStart]
      letterCount[char] -= 1
      windowStart += 1

    answer = max(answer, windowEnd - windowStart + 1)

  return answer

def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()
