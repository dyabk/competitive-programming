def brute_force(K, arr):
    results = []

    for ind in range(len(arr)):
        if ind + K <= len(arr):
            _sum = 0
            for x in range(ind, ind + K):
                _sum += arr[x]
            results.append(_sum / K);
        else:
            break

    return results;

def sliding_window(K, arr):
    pass

def main():
    result = brute_force(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()