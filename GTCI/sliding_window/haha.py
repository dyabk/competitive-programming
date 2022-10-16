from collections import Counter

def find_permutation(str1, pattern):
  pattern_length = len(pattern)
  pattern_count = [0] * 26

  for c in pattern:
    pattern_count[ord(c)-ord('a')] += 1

  window_count = [0]*26

  left = 0
  for right in range(len(str1)):
    window_count[ord(str1[right])-ord('a')] += 1

    if right - left + 1 > pattern_length:
      window_count[ord(str1[left])-ord('a')] -= 1
      left += 1
    
    if pattern_count == window_count:
      return True

  return False

def find_permutation(str1, pattern):
  pattern_length = len(pattern)
  cp = Counter(pattern)

  for i in range(len(str1) + 1):
    if i + pattern_length <= len(str1) and Counter(str1[i:i+pattern_length]) == cp:
      return True

  return False