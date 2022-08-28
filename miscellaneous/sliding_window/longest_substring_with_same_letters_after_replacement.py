from collections import Counter


def length_of_longest_substring(str1, k):

    max_repeat_letter_count = 0
    letter_freq = Counter()
    start = 0
    answer = 0

    for end in range(len(str1)):
        right_char = str1[end]
        if right_char not in letter_freq:
            letter_freq[right_char] = 0
        letter_freq[right_char] += 1

        max_repeat_letter_count = max(
            max_repeat_letter_count, letter_freq[right_char])

        if (end - start + 1 - max_repeat_letter_count) > k:
            left_char = str1[start]
            letter_freq[left_char] -= 1
            start += 1

        answer = max(answer, end - start + 1)

    return answer


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
