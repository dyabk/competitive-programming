from collections import Counter


def fruits_into_baskets(fruits):
    # TODO: Write your code here
    NUM_OF_BASKETS = 2
    baskets = Counter()
    answer = 0
    start = 0

    for end in range(len(fruits)):
        fruit = fruits[end]
        if fruit not in baskets:
            baskets[fruit] = 0
        baskets[fruit] += 1
        while len(baskets) > NUM_OF_BASKETS:
            baskets[fruits[start]] -= 1
            if baskets[fruits[start]] == 0:
                del baskets[fruits[start]]
            start += 1
        answer = max(answer, end - start + 1)
    return answer


def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
