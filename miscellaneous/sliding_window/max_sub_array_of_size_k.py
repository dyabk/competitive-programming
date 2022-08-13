def brute_force(k, arr):
  maxSum = 0
  for i in range(len(arr) - k + 1):
    curSum = sum(arr[i:i + k]);
    maxSum = max(maxSum, curSum)

  return maxSum

def sliding_window(k, arr):
  cur_sum, max_sum, window_start = 0, 0, 0
  for window_end in range(len(arr)):
    cur_sum += arr[window_end]
    if window_end >= k - 1:
      max_sum = max(max_sum, cur_sum)
      cur_sum -= arr[window_start]
      window_start += 1

  return max_sum

def main():
    print("Maximum sum of a subarray of size K: " + str(sliding_window(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(sliding_window(2, [2, 3, 4, 1, 5])))

main()