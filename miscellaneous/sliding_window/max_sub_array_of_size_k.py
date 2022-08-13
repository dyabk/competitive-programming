def brute_force(k, arr):
  maxSum = 0
  for i in range(len(arr) - k + 1):
    curSum = sum(arr[i:i + k]);
    maxSum = max(maxSum, curSum)

  return maxSum

def max_sub_array_of_size_k(k, arr):
  ans = float('-inf')
  windowStart, windowSum = 0, 0

  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]

    if windowEnd >= k - 1:
        ans = max(ans, windowSum)
        windowSum -= arr[windowStart]
        windowStart += 1

  return ans

def main():
    print("Maximum sum of a subarray of size K: " + str(brute_force(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(brute_force(2, [2, 3, 4, 1, 5])))

main()