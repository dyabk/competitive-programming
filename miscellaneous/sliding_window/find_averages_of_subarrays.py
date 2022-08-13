def brute_force(K, arr):
    results = []

    for i in range(len(arr) - K + 1):
        average = sum(arr[i:i+K]) / K;
        results.append(average);
    return results;

def sliding_window(K, arr):
    pass

def main():
    result = brute_force(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()