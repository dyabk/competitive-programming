def brute_force(K, arr):
    result = []

    for i in range(len(arr) - K + 1):
        average = sum(arr[i:i+K]) / 5
        result.append(average)

    return result

def sliding_window(K, arr):
    result = []

    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= arr[windowStart]
            windowStart += 1

    return result

def main():
    result = sliding_window(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()