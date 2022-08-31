from collections import Counter


def find_string_anagrams(str1, pattern):
    pattern_counter = Counter(pattern)
    result_indexes = []
    m = Counter()

    start = 0

    for end in range(len(str1)):
        m[str1[end]] += 1
        if end - start + 1 == len(pattern):
            if all(pattern_counter[chr] == m[chr] for chr in pattern_counter):
                result_indexes.append(start)
            m[str1[start]] -= 1
            start += 1

    return result_indexes
