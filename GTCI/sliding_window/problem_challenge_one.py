from collections import Counter


def find_permutation(str1, pattern):
    start = 0
    matched = 0
    patt_cnt = Counter(pattern)

    for end in range(len(str1)):
        right = str1[end]

        if right in patt_cnt:
            patt_cnt[right] -= 1
            if patt_cnt[right] == 0:
                matched += 1

        if matched == len(patt_cnt):
            return True

        while end - start + 1 - len(pattern) >= 0:
            left = str1[start]
            start += 1
            if left in patt_cnt:
                if patt_cnt[left] == 0:
                    matched -= 1
                patt_cnt[left] += 1

    return False
