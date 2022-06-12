def find_averages_of_subarrays(K, arr):
    result = []

    for i in range(len(arr) - K + 1):
        average = sum(arr[i:i+K]) / 5
        result.append(average)

    return result

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()