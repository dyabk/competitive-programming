from collections import Counter

def fruits_into_baskets(fruits):
  BASKETS = 2
  two_types = Counter()
  answer = 0

  windowStart = 0
  for windowEnd in range(len(fruits)):
    char = fruits[windowEnd]
    
    if char not in two_types:
      two_types[char] = 0
    two_types[char] += 1

    while len(two_types) > BASKETS:
      two_types[fruits[windowStart]] -= 1
      if two_types[fruits[windowStart]] == 0:
        del(two_types[fruits[windowStart]])
      windowStart += 1

    answer = max(answer, windowEnd - windowStart + 1)

  return answer

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()