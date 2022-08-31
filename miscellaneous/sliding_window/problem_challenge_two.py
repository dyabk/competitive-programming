from collections import Counter


def find_string_anagrams(str1, pattern):
    result_indexes = []
    pattern_map = Counter(pattern)
    start = 0
    matched = 0

    for end in range(len(str1)):
        right_chr = str1[end]
        if right_chr in pattern_map:
            pattern_map[right_chr] -= 1
            if pattern_map[right_chr] == 0:
                matched += 1

        if matched == len(pattern_map):
            result_indexes.append(start)

        while end - start + 1 >= len(pattern):
            left_chr = str1[start]
            if left_chr in pattern_map:
                if pattern_map[left_chr] == 0:
                    matched -= 1
                pattern_map[left_chr] += 1
            start += 1

    return result_indexes
