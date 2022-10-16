from collections import Counter


def longest_substring_with_k_distinct(str1, k):
    unique_characters = Counter()
    answer = 0

    start, end = 0, 0

    for end in range(len(str1)):
        character = str1[end]

        if character not in unique_characters:
            unique_characters[character] = 0
        unique_characters[character] += 1
        while len(unique_characters) > k:
            unique_characters[str1[start]] -= 1
            if unique_characters[str1[start]] == 0:
                del unique_characters[str1[start]]
            start += 1
        answer = max(answer, end - start + 1)
    return answer


def main():
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 10)))


main()
