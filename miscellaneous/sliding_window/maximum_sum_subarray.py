def max_sub_array_of_size_k(k, arr):
  ans = float('-inf')
  
  windowStart, windowSum = 0, 0

  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]

    if windowEnd >= k:
      windowSum -= arr[windowStart]
      windowStart += 1

      ans = max(ans, windowSum)

  return ans

def main():
    result1 = max_sub_array_of_size_k(k=3, arr=[2, 1, 5, 1, 3, 2])
    result2 = max_sub_array_of_size_k(k=2, arr=[2, 3, 4, 1, 5])
    print(result1)
    print(result2)

main()