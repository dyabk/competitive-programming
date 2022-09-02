from collections import Counter


def find_substring(str1, pattern):
    # TODO: Write your code here
    left, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1

    pc = Counter(pattern)
    for right in range(len(str1)):
        if str1[right] in pc:
            pc[str1[right]] -= 1
            if pc[str1[right]] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_length > right - left + 1:
                min_length = right - left + 1
                substr_start = left

            left_char = str1[left]
            left += 1
            if left_char in pc:
                if pc[left_char] == 0:
                    matched -= 1
                pc[left_char] += 1

    if min_length > len(str1):
        return ""

    return str1[substr_start:substr_start + min_length]
